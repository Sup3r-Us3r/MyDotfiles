#!/bin/bash

readonly PKGS_PACMAN=(
  i3 i3lock i3-gaps
  netctl dialog dhcpcd wireless_tools
  playerctl
  rofi
  picom
  termite
  zsh
  curl
  unzip
  feh
  nautilus
  xdg-user-dirs xdg-user-dirs-gtk xdg-utils
  leafpad
  lxappearance
  scrot
  python-mss
  git
  lm_sensors
  alsa-utils alsa-lib
  xorg-server xorg-xprop xorg-xinit xorg-xrandr arandr
  numlockx
  ttf-inconsolata ttf-fantasque-sans-mono)

readonly PKGS_AUR=(
  polybar
  siji-git)

function install_pkgs_pacman(){
  for i in "${PKGS_PACMAN[@]}"; do
    sudo pacman -S ${i} --needed --noconfirm
  done
}

function install_pkgs_aur(){
  for i in "${PKGS_AUR[@]}"; do
    yay -S ${i} --needed --noconfirm
  done
}

function install_yay(){
  if ! type -p yay > /dev/null
  then
    clear
    echo -e "INSTALL YAY\n"
    sleep 3
    cd $HOME
    sudo rm -rf $HOME/yay
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si --noconfirm
    cd ..
    sudo rm -rf $HOME/yay
  fi
}

function install_fonts(){
  clear
  echo -e "INSTALL POWERLINE FONTS AND FIRA CODE\n"
  sleep 3
  cd $HOME/Downloads/MyDotfiles
  sudo rm -rf fonts
  git clone https://github.com/powerline/fonts.git
  sh fonts/install.sh
  sudo rm -rf fonts
  sudo rm -rf .fonts/firacode/firacodeUnzip
  cd .fonts/firacode
  mkdir firacodeUnzip
  cp Fira_Code_v5.2.zip firacodeUnzip
  cd firacodeUnzip
  unzip Fira_Code_v5.2.zip
  sudo mv ttf/* /usr/share/fonts/TTF
  fc-cache -fv
}

function install_dotfiles(){
  clear
  echo -e "PREPARING THE ENVIRONMENT FOR DOTFILES\n"
  sleep 3
  cd $HOME
  xdg-user-dirs-update
  xdg-user-dirs-gtk-update
  cd $HOME/Downloads/MyDotfiles

  echo -e "\nINSTALL I3WM CONFIG\n"
  sleep 3
  sudo rm -rf $HOME/.config/i3
  mkdir -p $HOME/.config/i3
  cp -r .config/i3 $HOME/.config

  echo -e "\nINSTALL POLYBAR CONFIG\n"
  sleep 3
  sudo rm -rf $HOME/.config/polybar
  mkdir -p $HOME/.config/polybar
  cp -r .config/polybar $HOME/.config

  echo -e "\nINSTALL PICOM CONFIG\n"
  sleep 3
  sudo rm -rf $HOME/.config/picom
  mkdir -p $HOME/.config/picom
  cp -r .config/picom $HOME/.config

  echo -e "\nINSTALL ROFI CONFIG\n"
  sleep 3
  sudo rm -rf $HOME/.config/rofi
  mkdir -p $HOME/.config/rofi
  cp -r .config/rofi $HOME/.config

  echo -e "\nINSTALL TERMITE CONFIG\n"
  sleep 3
  sudo rm -rf $HOME/.config/termite
  sudo rm -rf $HOME/.config/gtk-3.0
  mkdir -p $HOME/.config/termite
  mkdir -p $HOME/.config/gtk-3.0
  cp -r .config/termite $HOME/.config
  cp -r .config/gtk-3.0 $HOME/.config

  echo -e "\nINSTALL .XINITRC CONFIG\n"
  sleep 3
  sudo rm -rf $HOME/.xinitrc
  cp .xinitrc $HOME/.xinitrc

  echo -e "\nINSTALL GENERAL USE SCRIPTS\n"
  sleep 3
  sudo rm -rf $HOME/scripts
  cp -r scripts $HOME

  echo -e "\nINSTALL GTK THEME\n"
  sleep 3
  sudo rm -rf dracula.zip
  sudo rm -rf dracula
  sudo rm -rf /usr/share/themes/dracula
  curl -s https://codeload.github.com/dracula/gtk/zip/master -o dracula.zip
  unzip dracula.zip
  mv gtk-master dracula
  sudo mv dracula /usr/share/themes

  echo -e "\nINSTALL ICON THEME\n"
  sleep 3
  sudo rm -rf /usr/share/icons/Numix-uTouch
  tar -xf .icons/Numix-uTouch.tar.gz
  sudo mv Numix-uTouch /usr/share/icons

  echo -e "\nINSTALL CURSOR THEME\n"
  sleep 3
  sudo rm -rf /usr/share/icons/ComixCursors*
  tar -Jxxvf .icons/xcursor-comix-0.9.0-3-any.pkg.tar.xz
  sudo mv usr/share/icons/ComixCursors* /usr/share/icons
  sudo rm -rf usr

  echo -e "\nAPPLY LAYOUT BR-ABNT2\n"
  sleep 3
  sudo rm -rf /etc/X11/xorg.conf.d
  sudo mkdir -p /etc/X11/xorg.conf.d
  sudo cp etc/X11/xorg.conf.d/00-keyboard.conf /etc/X11/xorg.conf.d
}

function config_setup(){
  clear
  echo -e "APPLY VOLUME 100%\n"
  sleep 3
  amixer set 'Master' 100% unmute
  sudo alsactl store

  echo -e "\nAPPLY CORRECT INTERFACE ON POLYBAR CONFIG\n"
  sleep 3
  ethernetInterface=`ls /sys/class/net | grep 'e'`
  wirelessInterface=`ls /sys/class/net | grep 'w'`
  sed -i "s/enp0s3/$ethernetInterface/g" $HOME/.config/polybar/config
  sed -i "s/enp0s3/$ethernetInterface/g" $HOME/.config/polybar/backup/config
  sed -i "s/wlp0s26u1u4/$wirelessInterface/g" $HOME/.config/polybar/config
  sed -i "s/wlp0s26u1u4/$wirelessInterface/g" $HOME/.config/polybar/backup/config

  echo -e "\nCONFIGURE EMAIL AND PASSWORD FOR GMAIL SCRIPT IN POLYBAR\n"
  sleep 3
  read -p "Email: " emailGmail
  sed -i "s/emailGmail/$emailGmail/g" $HOME/.config/polybar/scripts/mail
  read -p "Password: " passwordGmail
  sed -i "s/passwordGmail/$passwordGmail/g" $HOME/.config/polybar/scripts/mail

  echo -e "\nCONFIGURING PACMAN.CONF\n"
  sleep 3
  sudo sed -i '37iILoveCandy' /etc/pacman.conf
  sudo sed -i '/Color/,+1 s/^#//' /etc/pacman.conf

  echo -e "\nAPPLY WALLPAPER\n"
  if [ -d "$HOME/Pictures" ]; then
    cp wallpaper/wallpaper.jpg $HOME/Pictures
    feh --bg-scale $HOME/Pictures/wallpaper.jpg
  else
    cp wallpaper/wallpaper.jpg $HOME/Imagens
    feh --bg-scale $HOME/Imagens/wallpaper.jpg
    sed -i "s/Pictures/Imagens/g" $HOME/.config/i3/config
  fi
}

function oh-my-zsh(){
  clear
  echo -e "INSTALL OH-MY-ZSH\n"
  sleep 3
  cd $HOME
  sudo rm -rf $HOME/.oh-my-zsh
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
  git clone https://github.com/zsh-users/zsh-syntax-highlighting $HOME/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
  git clone https://github.com/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions
  git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"
  ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"
  cp $HOME/Downloads/MyDotfiles/.zshrc $HOME/.zshrc
}

function config_system(){
  clear
  echo -e "CONFIGURING GIT\n"
  sleep 3
  cd $HOME
  read -p "Git email: " gitEmail
  git config --global user.email ${gitEmail}
  read -p "Git name: " gitName
  git config --global user.name ${gitName}
}

install_pkgs_pacman
install_yay
install_pkgs_aur
install_fonts
install_dotfiles
config_setup
config_system
oh-my-zsh
