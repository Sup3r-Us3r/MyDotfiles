#!/usr/bin/env python


import getopt
import time
import errno
import os
import sys

# The following exits cleanly on Ctrl-C or EPIPE
# while treating other exceptions as before.
def std_exceptions(etype, value, tb):
    sys.excepthook = sys.__excepthook__
    if issubclass(etype, KeyboardInterrupt):
        pass
    elif issubclass(etype, IOError) and value.errno == errno.EPIPE:
        pass
    else:
        sys.__excepthook__(etype, value, tb)
sys.excepthook = std_exceptions

#
#   Define some global variables
#

PAGESIZE = os.sysconf("SC_PAGE_SIZE") / 1024 #KiB
our_pid = os.getpid()

have_pss = 0
have_swap_pss = 0

class Proc:
    def __init__(self):
        uname = os.uname()
        if uname[0] == "FreeBSD":
            self.proc = '/compat/linux/proc'
        else:
            self.proc = '/proc'

    def path(self, *args):
        return os.path.join(self.proc, *(str(a) for a in args))

    def open(self, *args):
        try:
            if sys.version_info < (3,):
                return open(self.path(*args))
            else:
                return open(self.path(*args), errors='ignore')
        except (IOError, OSError):
            val = sys.exc_info()[1]
            if (val.errno == errno.ENOENT or # kernel thread or process gone
                val.errno == errno.EPERM):
                raise LookupError
            raise

proc = Proc()


#
#   Functions
#

def parse_options():
    try:
        long_options = [
            'split-args',
            'help',
            'total',
            'discriminate-by-pid',
            'swap'
        ]
        opts, args = getopt.getopt(sys.argv[1:], "shtdSp:w:", long_options)
    except getopt.GetoptError:
        sys.stderr.write(help())
        sys.exit(3)

    if len(args):
        sys.stderr.write("Extraneous arguments: %s\n" % args)
        sys.exit(3)

    # ps_mem.py options
    split_args = False
    pids_to_show = None
    discriminate_by_pid = False
    show_swap = False
    watch = None
    only_total = False

    for o, a in opts:
        if o in ('-s', '--split-args'):
            split_args = True
        if o in ('-t', '--total'):
            only_total = True
        if o in ('-d', '--discriminate-by-pid'):
            discriminate_by_pid = True
        if o in ('-S', '--swap'):
            show_swap = True
        if o in ('-h', '--help'):
            sys.stdout.write(help())
            sys.exit(0)
        if o in ('-p',):
            try:
                pids_to_show = [int(x) for x in a.split(',')]
            except:
                sys.stderr.write(help())
                sys.exit(3)
        if o in ('-w',):
            try:
                watch = int(a)
            except:
                sys.stderr.write(help())
                sys.exit(3)

    return (
        split_args,
        pids_to_show,
        watch,
        only_total,
        discriminate_by_pid,
        show_swap
    )


def help():
    help_msg = 'Usage: ps_mem [OPTION]...\n' \
        'Show program core memory usage\n' \
        '\n' \
        '  -h, -help                   Show this help\n' \
        '  -p <pid>[,pid2,...pidN]     Only show memory usage PIDs in the '\
        'specified list\n' \
        '  -s, --split-args            Show and separate by, all command line'\
        ' arguments\n' \
        '  -t, --total                 Show only the total value\n' \
        '  -d, --discriminate-by-pid   Show by process rather than by program\n' \
        '  -S, --swap                  Show swap information\n' \
        '  -w <N>                      Measure and show process memory every'\
        ' N seconds\n'

    return help_msg


# (major,minor,release)
def kernel_ver():
    kv = proc.open('sys/kernel/osrelease').readline().split(".")[:3]
    last = len(kv)
    if last == 2:
        kv.append('0')
    last -= 1
    while last > 0:
        for char in "-_":
            kv[last] = kv[last].split(char)[0]
        try:
            int(kv[last])
        except:
            kv[last] = 0
        last -= 1
    return (int(kv[0]), int(kv[1]), int(kv[2]))


#return Private,Shared
#Note shared is always a subset of rss (trs is not always)
def getMemStats(pid):
    global have_pss
    global have_swap_pss
    mem_id = pid #unique
    Private_lines = []
    Shared_lines = []
    Pss_lines = []
    Rss = (int(proc.open(pid, 'statm').readline().split()[1])
           * PAGESIZE)
    Swap_lines = []
    Swap_pss_lines = []

    Swap = 0
    Swap_pss = 0

    if os.path.exists(proc.path(pid, 'smaps')):  # stat
        lines = proc.open(pid, 'smaps').readlines()  # open
        # Note we checksum smaps as maps is usually but
        # not always different for separate processes.
        mem_id = hash(''.join(lines))
        for line in lines:
            if line.startswith("Shared"):
                Shared_lines.append(line)
            elif line.startswith("Private"):
                Private_lines.append(line)
            elif line.startswith("Pss"):
                have_pss = 1
                Pss_lines.append(line)
            elif line.startswith("Swap:"):
                Swap_lines.append(line)
            elif line.startswith("SwapPss:"):
                have_swap_pss = 1
                Swap_pss_lines.append(line)
        Shared = sum([int(line.split()[1]) for line in Shared_lines])
        Private = sum([int(line.split()[1]) for line in Private_lines])
        #Note Shared + Private = Rss above
        #The Rss in smaps includes video card mem etc.
        if have_pss:
            pss_adjust = 0.5 # add 0.5KiB as this avg error due to truncation
            Pss = sum([float(line.split()[1])+pss_adjust for line in Pss_lines])
            Shared = Pss - Private
        # Note that Swap = Private swap + Shared swap.
        Swap = sum([int(line.split()[1]) for line in Swap_lines])
        if have_swap_pss:
            # The kernel supports SwapPss, that shows proportional swap share.
            # Note that Swap - SwapPss is not Private Swap.
            Swap_pss = sum([int(line.split()[1]) for line in Swap_pss_lines])
    elif (2,6,1) <= kernel_ver() <= (2,6,9):
        Shared = 0 #lots of overestimation, but what can we do?
        Private = Rss
    else:
        Shared = int(proc.open(pid, 'statm').readline().split()[2])
        Shared *= PAGESIZE
        Private = Rss - Shared
    return (Private, Shared, mem_id, Swap, Swap_pss)


def getCmdName(pid, split_args, discriminate_by_pid):
    cmdline = proc.open(pid, 'cmdline').read().split("\0")
    if cmdline[-1] == '' and len(cmdline) > 1:
        cmdline = cmdline[:-1]

    path = proc.path(pid, 'exe')
    try:
        path = os.readlink(path)
        # Some symlink targets were seen to contain NULs on RHEL 5 at least
        # https://github.com/pixelb/scripts/pull/10, so take string up to NUL
        path = path.split('\0')[0]
    except OSError:
        val = sys.exc_info()[1]
        if (val.errno == errno.ENOENT or # either kernel thread or process gone
            val.errno == errno.EPERM):
            raise LookupError
        raise

    if split_args:
        return " ".join(cmdline)
    if path.endswith(" (deleted)"):
        path = path[:-10]
        if os.path.exists(path):
            path += " [updated]"
        else:
            #The path could be have prelink stuff so try cmdline
            #which might have the full path present. This helped for:
            #/usr/libexec/notification-area-applet.#prelink#.fX7LCT (deleted)
            if os.path.exists(cmdline[0]):
                path = cmdline[0] + " [updated]"
            else:
                path += " [deleted]"
    exe = os.path.basename(path)
    cmd = proc.open(pid, 'status').readline()[6:-1]
    if exe.startswith(cmd):
        cmd = exe #show non truncated version
        #Note because we show the non truncated name
        #one can have separated programs as follows:
        #584.0 KiB +   1.0 MiB =   1.6 MiB    mozilla-thunder (exe -> bash)
        # 56.0 MiB +  22.2 MiB =  78.2 MiB    mozilla-thunderbird-bin
    if sys.version_info >= (3,):
        cmd = cmd.encode(errors='replace').decode()
    if discriminate_by_pid:
        cmd = '%s [%d]' % (cmd, pid)
    return cmd


#The following matches "du -h" output
#see also human.py
def human(num, power="Ki", units=None):
    if units is None:
        powers = ["Ki", "Mi", "Gi", "Ti"]
        while num >= 1000: #4 digits
            num /= 1024.0
            power = powers[powers.index(power)+1]
        return "%.1f %sB" % (num, power)
    else:
        return "%.f" % ((num * 1024) / units)


def cmd_with_count(cmd, count):
    if count > 1:
        return "%s (%u)" % (cmd, count)
    else:
        return cmd

#Warn of possible inaccuracies
#2 = accurate & can total
#1 = accurate only considering each process in isolation
#0 = some shared mem not reported
#-1= all shared mem not reported
def shared_val_accuracy():
    """http://wiki.apache.org/spamassassin/TopSharedMemoryBug"""
    kv = kernel_ver()
    pid = os.getpid()
    if kv[:2] == (2,4):
        if proc.open('meminfo').read().find("Inact_") == -1:
            return 1
        return 0
    elif kv[:2] == (2,6):
        if os.path.exists(proc.path(pid, 'smaps')):
            if proc.open(pid, 'smaps').read().find("Pss:")!=-1:
                return 2
            else:
                return 1
        if (2,6,1) <= kv <= (2,6,9):
            return -1
        return 0
    elif kv[0] > 2 and os.path.exists(proc.path(pid, 'smaps')):
        return 2
    else:
        return 1

def show_shared_val_accuracy( possible_inacc, only_total=False ):
    level = ("Warning","Error")[only_total]
    if possible_inacc == -1:
        sys.stderr.write("%s: Shared memory is not reported by this system.\n" % level)
        sys.stderr.write("Values reported will be too large, and totals are not reported\n")
    elif possible_inacc == 0:
        sys.stderr.write("%s: Shared memory is not reported accurately by this system.\n" % level)
        sys.stderr.write("Values reported could be too large, and totals are not reported\n")
    elif possible_inacc == 1:
        sys.stderr.write("%s: Shared memory is slightly over-estimated by this system\nfor each program, so totals are not reported.\n" % level)
    sys.stderr.close()
    if only_total and possible_inacc != 2:
        sys.exit(1)


def get_memory_usage(pids_to_show, split_args, discriminate_by_pid, include_self=False, only_self=False):
    cmds = {}
    shareds = {}
    mem_ids = {}
    count = {}
    swaps = {}
    shared_swaps = {}
    for pid in os.listdir(proc.path('')):
        if not pid.isdigit():
            continue
        pid = int(pid)

        # Some filters
        if only_self and pid != our_pid:
            continue
        if pid == our_pid and not include_self:
            continue
        if pids_to_show is not None and pid not in pids_to_show:
            continue

        try:
            cmd = getCmdName(pid, split_args, discriminate_by_pid)
        except LookupError:
            #operation not permitted
            #kernel threads don't have exe links or
            #process gone
            continue

        try:
            private, shared, mem_id, swap, swap_pss = getMemStats(pid)
        except RuntimeError:
            continue #process gone
        if shareds.get(cmd):
            if have_pss: #add shared portion of PSS together
                shareds[cmd] += shared
            elif shareds[cmd] < shared: #just take largest shared val
                shareds[cmd] = shared
        else:
            shareds[cmd] = shared
        cmds[cmd] = cmds.setdefault(cmd, 0) + private
        if cmd in count:
            count[cmd] += 1
        else:
            count[cmd] = 1
        mem_ids.setdefault(cmd, {}).update({mem_id: None})

        # Swap (overcounting for now...)
        swaps[cmd] = swaps.setdefault(cmd, 0) + swap
        if have_swap_pss:
            shared_swaps[cmd] = shared_swaps.setdefault(cmd, 0) + swap_pss
        else:
            shared_swaps[cmd] = 0

    # Total swaped mem for each program
    total_swap = 0

    # Total swaped shared mem for each program
    total_shared_swap = 0

    # Add shared mem for each program
    total = 0

    for cmd in cmds:
        cmd_count = count[cmd]
        if len(mem_ids[cmd]) == 1 and cmd_count > 1:
            # Assume this program is using CLONE_VM without CLONE_THREAD
            # so only account for one of the processes
            cmds[cmd] /= cmd_count
            if have_pss:
                shareds[cmd] /= cmd_count
        cmds[cmd] = cmds[cmd] + shareds[cmd]
        total += cmds[cmd]  # valid if PSS available
        total_swap += swaps[cmd]
        if have_swap_pss:
            total_shared_swap += shared_swaps[cmd]

    sorted_cmds = sorted(cmds.items(), key=lambda x:x[1])
    sorted_cmds = [x for x in sorted_cmds if x[1]]

    return sorted_cmds, shareds, count, total, swaps, shared_swaps, \
        total_swap, total_shared_swap


def print_header(show_swap, discriminate_by_pid):
    output_string = " Private  +   Shared  =  RAM used"
    if show_swap:
        if have_swap_pss:
            output_string += " " * 5 + "Shared Swap"
        output_string += "   Swap used"
    output_string += "\tProgram"
    if discriminate_by_pid:
        output_string += "[pid]"
    output_string += "\n\n"
    sys.stdout.write(output_string)


def print_memory_usage(sorted_cmds, shareds, count, total, swaps, total_swap, shared_swaps, total_shared_swap, show_swap):
    for cmd in sorted_cmds:

        output_string = "%9s + %9s = %9s"
        output_data = (human(cmd[1]-shareds[cmd[0]]), human(shareds[cmd[0]]), human(cmd[1]))
        if show_swap:
            if have_swap_pss:
                output_string += "\t%9s"
                output_data += (human(shared_swaps[cmd[0]]),)
            output_string += "   %9s"
            output_data += (human(swaps[cmd[0]]),)
        output_string += "\t%s\n"
        output_data += (cmd_with_count(cmd[0], count[cmd[0]]),)

        sys.stdout.write(output_string % output_data)

    if have_pss:
        if show_swap:
            if have_swap_pss:
                sys.stdout.write("%s\n%s%9s%s%9s%s%9s\n%s\n" %
                                 ("-" * 61, " " * 24, human(total), " " * 7,
                                  human(total_shared_swap), " " * 3,
                                  human(total_swap), "=" * 61))
            else:
                sys.stdout.write("%s\n%s%9s%s%9s\n%s\n" %
                                 ("-" * 45, " " * 24, human(total), " " * 3,
                                  human(total_swap), "=" * 45))
        else:
            sys.stdout.write("%s\n%s%9s\n%s\n" %
                             ("-" * 33, " " * 24, human(total), "=" * 33))


def verify_environment():
    if os.geteuid() != 0:
        sys.stderr.write("Sorry, root permission required.\n")
        sys.stderr.close()
        sys.exit(1)

    try:
        kernel_ver()
    except (IOError, OSError):
        val = sys.exc_info()[1]
        if val.errno == errno.ENOENT:
            sys.stderr.write(
              "Couldn't access " + proc.path('') + "\n"
              "Only GNU/Linux and FreeBSD (with linprocfs) are supported\n")
            sys.exit(2)
        else:
            raise

def main():
    split_args, pids_to_show, watch, only_total, discriminate_by_pid, \
    show_swap = parse_options()

    verify_environment()

    if not only_total:
        print_header(show_swap, discriminate_by_pid)

    if watch is not None:
        try:
            sorted_cmds = True
            while sorted_cmds:
                sorted_cmds, shareds, count, total, swaps, shared_swaps, \
                    total_swap, total_shared_swap = \
                    get_memory_usage(pids_to_show, split_args, discriminate_by_pid)
                if only_total and have_pss:
                    sys.stdout.write(human(total, units=1)+'\n')
                elif not only_total:
                    print_memory_usage(sorted_cmds, shareds, count, total, swaps, total_swap, shared_swaps, total_shared_swap, show_swap)

                sys.stdout.flush()
                time.sleep(watch)
            else:
                sys.stdout.write('Process does not exist anymore.\n')
        except KeyboardInterrupt:
            pass
    else:
        # This is the default behavior
        sorted_cmds, shareds, count, total, swaps, shared_swaps, total_swap, \
            total_shared_swap = get_memory_usage(pids_to_show, split_args, discriminate_by_pid)
        if only_total and have_pss:
            sys.stdout.write(human(total, units=1)+'\n')
        elif not only_total:
            print_memory_usage(sorted_cmds, shareds, count, total, swaps, total_swap, shared_swaps, total_shared_swap, show_swap)

    # We must close explicitly, so that any EPIPE exception
    # is handled by our excepthook, rather than the default
    # one which is reenabled after this script finishes.
    sys.stdout.close()

    vm_accuracy = shared_val_accuracy()
    show_shared_val_accuracy( vm_accuracy, only_total )

if __name__ == '__main__': main()