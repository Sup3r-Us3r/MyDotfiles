#!/bin/sh
#
# ufetch-arch - tiny system info for arch

## INFO

# user is already defined
host="$(hostname)"
os='Arch Linux'
kernel="$(uname -sr)"
uptime="$(uptime -p | sed 's/up //')"
packages="$(pacman -Q | wc -l)"
shell="$(basename ${SHELL})"

if [ -z "${WM}" ]; then
	if [ "${XDG_CURRENT_DESKTOP}" ]; then
		envtype='DE'
		WM="${XDG_CURRENT_DESKTOP}"
	elif [ "${DESKTOP_SESSION}" ]; then
		envtype='DE'
		WM="${DESKTOP_SESSION}"
	else
		envtype='WM'
		WM="i3gaps"
	fi
else
	envtype='WM'
fi

## DEFINE COLORS

# probably don't change these
bold="$(tput bold)"
black="$(tput setaf 0)"
red="$(tput setaf 1)"
green="$(tput setaf 2)"
yellow="$(tput setaf 3)"
blue="$(tput setaf 4)"
magenta="$(tput setaf 5)"
cyan="$(tput setaf 6)"
white="$(tput setaf 7)"
reset="$(tput sgr0)"

# you can change these
lc="${reset}${bold}${magenta}"		# labels
nc="${reset}${bold}${magenta}"		# user and hostname
ic="${reset}${bold}${white}"	# info
c0="${reset}${bold}${magenta}"		# first color
c1="${reset}${magenta}"			# second color

## OUTPUT

cat <<EOF

${ic}        /\        ${nc}${USER}${ic}@${nc}${host}${reset}
${ic}       /^^\       ${lc}OS:        ${ic}${os}${reset}
${ic}      /\   \      ${lc}KERNEL:    ${ic}${kernel}${reset}
${ic}     /  ${ic}__  \     ${lc}UPTIME:    ${ic}${uptime}${reset}
${ic}    /  (  )  \    ${lc}PACKAGES:  ${ic}${packages}${reset}
${ic}   / __|  |__\\\\   ${lc}SHELL:     ${ic}${shell}${reset}
${ic}  ///        \\\\\  ${lc}${envtype}:        ${ic}${WM}${reset}

EOF
