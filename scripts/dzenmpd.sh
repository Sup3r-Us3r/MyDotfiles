#! /bin/sh

position(){
pos=$(mpc | awk 'NR==2' | awk '{print $4}' | sed 's/(//' | sed 's/%)//')
bar=$(echo $pos | gdbar -w 190 -h 5 -fg "#FF5555" -bg "#FFFFFF")
echo -n "$bar"
return
}

font="M+ 1c-7.5"
icon="/home/ghost/.icons/xbm8x8"

while :; do
echo "   $(mpc current -f %artist%)
   $(mpc current -f %title%) 
   $(mpc current -f %album%)

^p(65)^ca(1,mpc prev)^i($icon/prev.xbm)^ca()   ^ca(1,mpc play)^i($icon/play.xbm)^ca()   ^ca(1,mpc pause)^i($icon/pause.xbm)^ca()   ^ca(1,mpc stop)^i($icon/stop.xbm)^ca()   ^ca(1,mpc next)^i($icon/next.xbm)^ca()
$(position)" 
done | dzen2 -p -y 100 -x 1720 -l 5 -u -w 190 -ta l -fn "$font" -e 'onstart=uncollapse;button3=exit'
