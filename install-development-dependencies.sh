#!/bin/bash

readonly PKGS_PACMAN=(
  npm
  yarn
  docker
  docker-compose
  jdk8-openjdk
  unzip)

readonly PKGS_AUR=(
  visual-studio-code-bin
  insomnia
  robo3t-bin
  reactotron)

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

function install_vscode_extensions(){
  clear
  echo -e "INSTALL VSCODE EXTENSIONS\n"
  sleep 3
  cd $HOME
  code --install-extension abusaidm.html-snippets
  code --install-extension bradlc.vscode-tailwindcss
  code --install-extension dbaeumer.vscode-eslint
  code --install-extension EditorConfig.EditorConfig
  code --install-extension esbenp.prettier-vscode
  code --install-extension formulahendry.code-runner
  code --install-extension rocketseat.theme-omni
  code --install-extension alexcvzz.vscode-sqlite
  code --install-extension dart-code.dart-code
  code --install-extension dart-code.flutter
  code --install-extension jpoissonnier.vscode-styled-components
  code --install-extension leizongmin.node-module-intellisense
  code --install-extension mikestead.dotenv
  code --install-extension naumovs.color-highlight
  code --install-extension oderwat.indent-rainbow
  code --install-extension PKief.material-icon-theme
  code --install-extension Prisma.vscode-graphql
  code --install-extension ritwickdey.LiveServer
  code --install-extension VisualStudioExptTeam.vscodeintellicode
}

function install_vscode_config(){
  clear
  echo -e "VSCODE SETTINGS.JSON CONFIG\n"
  sleep 3
  cd $HOME/Downloads/MyDotfiles
  sudo rm -rf $HOME/.config/Code/User/settings.json
  mkdir -p $HOME/.config/Code/User
  cp .config/Code/User/settings.json $HOME/.config/Code/User/settings.json
}

function configure_docker(){
  clear
  echo -e "DOCKER CONFIGURATION\n"
  sleep 3
  cd $HOME
  sudo gpasswd -a $USER docker
  sudo systemctl start docker
  export DOCKER_HOST=127.0.0.1:2375
  sudo systemctl restart docker
}

function mobile_enviroment(){
  clear
  echo -e "PREPARING MOBILE ENVIRONMENT\n"
  sleep 3
  cd $HOME
  sudo archlinux-java set java-8-openjdk
  sudo rm -rf $HOME/.Android
  sudo rm -rf $HOME/.android
  mkdir -p $HOME/.Android/Sdk
  sudo rm -rf getAndroidStudioDataForDownload.txt
  sudo rm -rf android-studio.tar.gz
  sudo rm -rf .android-studio
  curl -o getAndroidStudioDataForDownload.txt https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=android-studio
  pkgver=`sed -nr "s/^pkgver=([^=]+)$/\1/p" getAndroidStudioDataForDownload.txt`
  build=`sed -nr "s/^_build=([^=]+)$/\1/p" getAndroidStudioDataForDownload.txt`
  curl -o android-studio.tar.gz https://dl.google.com/dl/android/studio/ide-zips/$pkgver/android-studio-ide-$build-linux.tar.gz
  tar -xf android-studio.tar.gz
  mv android-studio .android-studio
  echo "Continue installing Android Studio"
  echo "https://react-native.rocketseat.dev/android/linux"
}

install_pkgs_pacman
install_pkgs_aur
install_vscode_extensions
install_vscode_config
configure_docker
mobile_enviroment
