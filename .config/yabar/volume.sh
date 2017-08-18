#!/bin/bash
mute=`amixer get Master | grep "Front Left:" | awk '{print $6}'`
vol=`amixer get Master | grep "Front Left:" | awk '{print $5}' | tr -d '[%]'`
if [ $mute == "[on]" ]
then
    if [ $vol -eq 100 ]
    then 
        echo "  $vol"
    elif [ $vol -ge 50 ]
    then 
        echo "   $vol"
    elif [ $vol -lt 50 ]
    then
        if [ $vol -lt 10 ]
        then
            echo "       $vol"
        else 
            echo "    $vol"
        fi
    else
        :
    fi
else
    echo "  Muted " 
fi