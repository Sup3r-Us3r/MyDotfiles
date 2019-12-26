#!/bin/bash

# ALL DEPENDENCIES
#sudo pacman -S i3 i3lock lm_sensors hddtemp playerctl leafpad termite compton nautilus feh mpc alsa-lib alsa-utils mpd ncmpcpp conky scrot nitrogen rofi lxappearance wireless_tools zsh git ttf-dejavu
#yay -S polybar i3blocks dmenu2 lemonbar-git dmenu2 lemonbar-git i3-gaps ttf-inconsolata ttf-font-awesome ttf-fantasque-sans-mono siji-git

# REQUIRED DEPENDENCIES
echo "INSTALLING DEPENDENCE NEEDED FOR SETTINGS\n"
sudo pacman -S i3 i3lock lm_sensors playerctl leafpad termite compton nautilus feh alsa-lib alsa-utils scrot rofi lxappearance wireless_tools zsh git ttf-dejavu
yay -S polybar i3-gaps ttf-inconsolata ttf-fantasque-sans-mono siji-git

clear

echo "INSTALLING POWERLINE FONTS\n"
git clone https://github.com/powerline/fonts.git && sleep 2 && sh fonts/install.sh
