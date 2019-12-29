#!/bin/bash

readonly PKGS_XBPS=(
    i3 i3lock i3-gaps
    polybar
    rofi
    picom
    lxterminal
    zsh
    curl
    feh
    nautilus
    leafpad
    lxappearance
    scrot
    git
    lm_sensors
    alsa-utils alsa-lib
    dejavu-fonts-ttf font-inconsolata-otf font-fantasque-sans-ttf font-Siji
    xdg-user-dirs xdg-user-dirs-gtk)

#readonly PKGS_XBPSSRC=()

function install_pkgs_xbps(){
    for i in "${PKGS_XBPS[@]}"; do
        sudo xbps-install -S ${i}
    done
}

#function install_pkgs_xbpssrc(){}

function install_powerline_fonts(){
    clear
    echo -e "INSTALANDO FONTES POWERLINE\n"
    sleep 3
    cd $HOME
    sudo rm -rf fonts
    git clone https://github.com/powerline/fonts.git
    sh fonts/install.sh
    sudo rm -rf fonts
}

function install_dotfiles(){
    clear
    echo -e "PREPARANDO AMBIENTE PARA AS DOTFILES\n"
    sleep 3
    cd $HOME
    xdg-user-dirs-update
    xdg-user-dirs-gtk-update
    cd $HOME/Downloads
    #git clone https://github.com/Sup3r-Us3r/MyDotfiles.git
    cd MyDotfiles

    echo -e "\nINSTALANDO CONFIGURAÇÃO DO I3WM\n"
    sleep 3
    sudo rm -rf $HOME/.config/i3
    mkdir -p $HOME/.config/i3
    cp -r .config/i3 $HOME/.config

    echo -e "\nINSTALANDO CONFIGURAÇÃO DO POLYBAR\n"
    sleep 3
    sudo rm -rf $HOME/.config/polybar
    mkdir -p $HOME/.config/polybar
    cp -r .config/polybar $HOME/.config

    echo -e "\nINSTALANDO CONFIGURAÇÃO DO PICOM\n"
    sleep 3
    sudo rm -rf $HOME/.config/picom
    mkdir -p $HOME/.config/picom
    cp -r .config/picom $HOME/.config

    echo -e "\nINSTALANDO CONFIGURAÇÃO DO ROFI\n"
    sleep 3
    sudo rm -rf $HOME/.config/rofi
    mkdir -p $HOME/.config/rofi
    cp -r .config/rofi $HOME/.config
    sudo cp $HOME/.config/rofi/usr/share/rofi/themes/sup3r-us3r-theme.rasi /usr/share/rofi/themes/sup3r-us3r-theme.rasi

    echo -e "\nINSTALANDO CONFIGURAÇÃO DO LXTERMINAL\n"
    sleep 3
    sudo rm -rf $HOME/.config/lxterminal
    mkdir -p $HOME/.config/lxterminal
    cp -r .config/lxterminal $HOME/.config

    echo -e "\nINSTALANDO CONFIGURAÇÃO DO .XINITRC\n"
    sleep 3
    sudo rm -rf $HOME/.xinitrc
    cp .xinitrc $HOME/.xinitrc

    echo -e "\nINSTALANDO SCRIPTS DE USO GERAL\n"
    sleep 3
    sudo rm -rf $HOME/scripts
    cp -r scripts $HOME

    echo -e "\nINSTALANDO TEMA GTK\n"
    sleep 3
    sudo rm -rf /usr/share/themes/Sweet-Dark
    tar -Jxxvf .themes/Sweet-Dark.tar.xz
    sudo mv Sweet-Dark /usr/share/themes

    echo -e "\nINSTALANDO TEMA DE ÍCONES\n"
    sleep 3
    sudo rm -rf /usr/share/icons/Numix-uTouch
    tar -xf .icons/Numix-uTouch.tar.gz
    sudo mv Numix-uTouch /usr/share/icons

    echo -e "\nINSTALANDO TEMA DE CURSOR\n"
    sleep 3
    sudo rm -rf /usr/share/icons/ComixCursors*
    tar -Jxxvf .icons/xcursor-comix-0.9.0-3-any.pkg.tar.xz
    sudo mv usr/share/icons/ComixCursors* /usr/share/icons
    sudo rm -rf usr

    echo -e "\nSETANDO LAYOUT BR-ABNT2\n"
    sleep 3
    sudo rm -rf /etc/X11/xorg.conf.d
    sudo mkdir -p /etc/X11/xorg.conf.d
    sudo cp etc/X11/xorg.conf.d/10-keyboard.conf /etc/X11/xorg.conf.d
}

function config_setup(){
    clear
    echo -e "SETANDO 100% DE VOLUME\n"
    sleep 3
    amixer sset 'Master' 100%
    sudo alsactl store

    echo -e "\nSETANDO INTERFACE DE REDE WIRELESS NO POLYBAR\n"
    sleep 3
    interfaceWireless=`ip -o addr show scope global | awk '{split($4, a, "/"); print $2}'`
    sed -i "s/wlp0s26u1u4/$interfaceWireless/g" $HOME/.config/polybar/config
    sed -i "s/wlp0s26u1u4/$interfaceWireless/g" $HOME/.config/polybar/backup/config
}

function oh-my-zsh(){
    clear
    echo -e "INSTALANDO OH-MY-ZSH\n"
    sleep 3
    sudo rm -rf $HOME/.oh-my-zsh
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
    #git clone https://github.com/zsh-users/zsh-syntax-highlighting $HOME/.oh-my-zsh/custom/plugins
    #cd $HOME/Downloads/MyDotfiles
    #cp .zshrc $HOME/.zshrc
    #source ~/.zshrc
}

function config_system(){
    clear
    echo -e "CONFIGURANDO GIT\n"
    sleep 3
    cd $HOME
    git config --global user.email "pc.gam3rs.tuto@gmail.com"
    git config --global user.name "Sup3r-Us3r"
}

install_pkgs_xbps
install_powerline_fonts
install_dotfiles
config_setup
config_system
oh-my-zsh
