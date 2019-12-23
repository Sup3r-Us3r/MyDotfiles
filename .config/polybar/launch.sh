#!/usr/bin/env sh

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -x polybar > /dev/null; do sleep 1; done

# Wal Config
#source "${HOME}/.cache/wal/colors.sh"
#background=$color0
#background_alt=$color3
#foreground=$color15
#foreground_alt=$color2
#highlight=$color4

polybar -r arch &
