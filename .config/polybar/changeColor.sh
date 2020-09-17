#!/bin/bash

read -p "Bar color: " barColor
lastBarColor=`cat .colorsData | grep 'barColor' | awk '{print $3}'`
sed -i "s/$lastBarColor/$barColor/g" $HOME/.config/polybar/config
sed -i "s/$lastBarColor/$barColor/g" $HOME/.config/polybar/.colorsData

read -p "Workspace color: " workspaceColor
lastWorkspaceColor=`cat .colorsData | grep 'workspaceColor' | awk '{print $3}'`
sed -i "s/$lastWorkspaceColor/$workspaceColor/g" $HOME/.config/polybar/config
sed -i "s/$lastWorkspaceColor/$workspaceColor/g" $HOME/.config/polybar/.colorsData

read -p "Icons color: " iconsColor
lastIconsColor=`cat .colorsData | grep 'iconsColor' | awk '{print $3}'`
sed -i "s/$lastIconsColor/$iconsColor/g" $HOME/.config/polybar/config
sed -i "s/$lastIconsColor/$iconsColor/g" $HOME/.config/polybar/.colorsData

read -p "Text color: " textColor
lastTextColor=`cat .colorsData | grep 'textColor' | awk '{print $3}'`
sed -i "s/$lastTextColor/$textColor/g" $HOME/.config/polybar/config
sed -i "s/$lastTextColor/$textColor/g" $HOME/.config/polybar/.colorsData
