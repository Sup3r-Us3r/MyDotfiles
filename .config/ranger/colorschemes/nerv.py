from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Nerv(ColorScheme):
    progress_bar_color = red

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            fg = white
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                fg = 240
            if context.border:
                fg = default
            if context.media:
                if context.image:
                    fg = blue
                elif context.video:
                    fg = magenta
                elif context.audio:
                    fg = cyan
                elif context.document:
                    fg = green
                else:
                    fg = white
            if context.container:
                fg = white
                bg = cyan 
            if context.directory:
                fg = red  
            elif context.executable and not \
                    any((context.media, context.container,
                        context.fifo, context.socket)):
                fg = yellow
                attr |= bold
            if context.socket:
                fg = 136
                bg = 230
                attr |= bold
            if context.fifo:
                fg = 133
                bg = 230
                attr |= bold
            if context.device:
                fg = 244
                bg = 230
                attr |= bold
            if context.link:
                fg = context.good and 11 or 160
                attr |= bold
                if context.bad:
                    bg = 235
            if context.tag_marker and not context.selected:
                attr |= bold
                if fg in (red, magenta):
                    fg = white
                else:
                    fg = red
            if not context.selected and (context.cut or context.copied):
                fg = 234
                attr |= bold
            if context.main_column:
                if context.selected:
                    attr |= bold
                if context.marked:
                    attr |= bold
                    bg = 237
            if context.badinfo:
                if attr & reverse:
                    bg = magenta
                else:
                    fg = magenta

        elif context.in_titlebar:
            attr |= bold 
            bg = black  
            if context.hostname:
                if context.bad:
                    fg = red
            elif context.directory:
                fg = yellow
            elif context.tab:
                if context.good:
                    attr |= reverse
            elif context.link:
                fg = blue 

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = cyan  
                elif context.bad:
                    fg = white
                    bg = red
            if context.marked:
                attr |= bold | reverse
                fg = yellow
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = red
            if context.loaded:
                bg = self.progress_bar_color

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = default

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        return fg, bg, attr
