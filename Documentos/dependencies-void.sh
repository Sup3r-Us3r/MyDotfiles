#!/bin/bash

# REQUIRED DEPENDENCIES
echo "INSTALLING DEPENDENCE NEEDED FOR SETTINGS\n"
sudo xbps-install i3 i3lock lm_sensors playerctl leafpad lxterminal picom nautilus feh alsa-lib alsa-utils scrot rofi lxappearance zsh git dejavu-fonts-ttf polybar i3-gaps font-inconsolata-otf font-fantasque-sans-ttf font-Siji

clear

echo "INSTALLING POWERLINE FONTS\n"
git clone https://github.com/powerline/fonts.git && sleep 2 && sh fonts/install.sh
