#!/bin/sh

#-------------------------------# 
#  ╻ ╻╻┏┓╻╻╺┳╸┏━┓┏━╸            #
#  ┏╋┛┃┃┗┫┃ ┃ ┣┳┛┃              #
# ╹╹ ╹╹╹ ╹╹ ╹ ╹┗╸┗━╸            #
# by Sup3r-Us3r                 #
# no login manager since forever#
#-------------------------------#

##----------------------------------------------------------------------------##
## Launch dbus 
##----------------------------------------------------------------------------##

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

##----------------------------------------------------------------------------##
## Mpd autostart 
##----------------------------------------------------------------------------##

[ !  -s ~/.config/mpd/pid ] && mpd


##----------------------------------------------------------------------------##
## Update Xresources 
##----------------------------------------------------------------------------##

[[ -f ~/.Xresources ]] && xrdb -merge "${HOME}/.Xresources"

##----------------------------------------------------------------------------##
## My fonts   
##----------------------------------------------------------------------------##

xset +fp ~/.fonts
xset +fp /usr/share/fonts/local 
xset fp rehash
xset -dpms
xset s off


##----------------------------------------------------------------------------##
## General settings 
##----------------------------------------------------------------------------##
xsetroot -cursor_name left_ptr
urxvtd -q -o -f
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
nitrogen --restore &
compton --config ~/.config/compton.conf  &
udiskie &
unclutter &

##----------------------------------------------------------------------------##
## startx
##----------------------------------------------------------------------------##

_start_session() {
  session=${1:-i3}
  case $session in
      awesome           ) exec awesome;;
      bspwm             ) exec bspwm;;
      xmonad            ) exec xmonad;;
      dwm               ) exec dwm;;
      bspwm             ) exec bspwm;;
      2bwm              ) exec 2bwm ;;
      i3|i3wm           ) exec i3;;
      mate              ) exec mate-session;;
      openbox           ) exec openbox-session;;
      xfce|xfce4        ) exec startxfce4;;
      # No known session, try to run it as command
      *) exec "$1";;
  esac
}
_start_session "$@"





