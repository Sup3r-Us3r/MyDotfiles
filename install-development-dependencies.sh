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
  reactotron
  genymotion)

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
  echo -e "INSTALANDO EXTENSÕES DO VSCODE\n"
  sleep 3
  cd $HOME
  code --install-extension abusaidm.html-snippets
  code --install-extension bradlc.vscode-tailwindcss
  code --install-extension dbaeumer.vscode-eslint
  code --install-extension dracula-theme.theme-dracula
  code --install-extension EditorConfig.EditorConfig
  code --install-extension esbenp.prettier-vscode
  code --install-extension formulahendry.code-runner
  code --install-extension jaccon.punk-dark-theme
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
  echo -e "SETANDO SETTINGS.JSON NO VSCODE\n"
  sleep 3
  cd $HOME/Downloads/MyDotfiles
  sudo rm -rf $HOME/.config/Code/User/settings.json
  mkdir -p $HOME/.config/Code/User
  cp .config/Code/User/settings.json $HOME/.config/Code/User/settings.json
}

function configure_docker(){
  clear
  echo -e "CONFIGURANDO DOCKER\n"
  sleep 3
  cd $HOME
  sudo gpasswd -a $USER docker
  sudo systemctl start docker
  export DOCKER_HOST=127.0.0.1:2375
  sudo systemctl restart docker
}

function react_native_enviroment(){
  clear
  echo -e "CRIANDO E CONFIGURANDO AMBIENTE DE DESENVOLVIMENTO REACT NATIVE\n"
  sleep 3
  cd $HOME
  yarn global add react-native-cli
  sudo archlinux-java set java-8-openjdk
  sudo rm -rf $HOME/.Android
  sudo rm -rf $HOME/.android
  mkdir -p $HOME/.Android/Sdk
  curl -o sdk-tools-linux.zip https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip
  unzip sdk-tools-linux.zip
  mv tools $HOME/.Android/Sdk
  ~/Android/Sdk/tools/bin/sdkmanager "platform-tools" "platforms;android-27" "build-tools;27.0.3"
  sudo vboxreload
  echo -e "
    1º Configurar SDK customizada
      - Abra o Genymotion
      - Genymotion -> Settings -> ADB -> Use Custom Android SDK tools -> /home/SEU_USUÁRIO/.Android/Sdk

    2º Conectar emulador ao ADB (Android Debug Bridge)
      - adb connect IP_DO_SEU_EMULADOR:5555
      - adb devices
  "
}

install_pkgs_pacman
install_pkgs_aur
install_vscode_extensions
install_vscode_config
configure_docker
react_native_enviroment
