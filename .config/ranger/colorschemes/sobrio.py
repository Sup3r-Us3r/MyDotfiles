from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Default(ColorScheme):
	def use(self, context):
		fg, bg, attr = default_colors

		if context.reset:
			return default_colors

		elif context.in_browser:
			if context.selected:
				fg = white
				attr = bold
			else:
				attr = normal
			if context.empty or context.error:
				fg = yellow
			if context.border:
				attr = normal
				fg = yellow
			if context.media:
				if context.image:
					fg = yellow
				else:
					fg = white
			if context.container:
				attr |= normal
				fg = green
			if context.directory:
				attr |= normal
				fg = red
			elif context.executable and not \
					any((context.media, context.container,
						context.fifo, context.socket)):
				attr |= normal
				fg = red
			if context.socket:
				fg = red
			if context.fifo or context.device:
				fg = yellow
				if context.device:
					attr |= bold
			if context.link:
				fg = context.good and white or red
			if context.tag_marker and not context.selected:
				attr |= bold
				if fg in (red, white):
					fg = yellow
				else:
					fg = green
			if not context.selected and (context.cut or context.copied):
				fg = white
				attr |= bold
			if context.main_column:
				if context.selected:
					attr |= normal
				if context.marked:
					attr |= underline
					fg = white
			if context.badinfo:
				if attr & reverse:
					bg = red
				else:
					fg = red

		elif context.in_titlebar:
			attr |= normal
			if context.hostname:
				attr |= normal
				fg = red
			elif context.directory:
				fg = red
			elif context.tab:
				if context.good:
					bg = green
			elif context.link:
				fg = magenta

		elif context.in_statusbar:
			if context.permissions:
				if context.good:
					fg = yellow
				elif context.bad:
					fg = red
			if context.marked:
				attr |= bold | reverse
				fg = yellow
			if context.message:
				if context.bad:
					attr |= bold
					fg = red

		if context.text:
			if context.highlight:
				attr |= bold

		if context.in_taskview:
			if context.title:
				fg = red

			if context.selected:
				attr |= normal

		return fg, bg, attr
