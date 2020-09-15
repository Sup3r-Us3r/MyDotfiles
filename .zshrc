# PATH TO YOUR OH-MY-ZSH INSTALLATION
export ZSH=/home/$USER/.oh-my-zsh

# ZSH_THEME
ZSH_THEME="agnoster"

# PLUGINS
# PATH CUSTOM PLUGINS: ~/.oh-my-zsh/custom/plugins
plugins=(git zsh-syntax-highlighting)

# RELOAD CONFIG
source $ZSH/oh-my-zsh.sh

# MY ALIASES
alias pac="sudo pacman -S"
alias psyu="sudo pacman -Syyu --noconfirm"
alias pacr="sudo pacman -Rnsc"
alias paco="sudo pacman -Sc"
alias pacsearch="pacman -Sl | cut -d' ' -f2 | grep"
alias cleaning="sudo rm -rf /var/cache/pacman/pkg/*.*"
alias weather="curl http://wttr.in/itabira"
alias sf="screenfetch | lolcat"
alias ufetch="~/scripts/ufetch-arch.sh"
alias infosystem="~/scripts/info-i3.sh"
alias leafpad="leafpad 2>/dev/null"
alias postbird="/snap/bin/postbird 2>/dev/null"
alias q="exit"

# PYWAL
#export PATH="${PATH}:${HOME}/.local/bin/"
#cat ~/.cache/wal/sequences

# ANDROID STUDIO
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk
export ANDROID_HOME=~/.Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:~/.android-studio/bin
