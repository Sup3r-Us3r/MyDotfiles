# PATH TO YOUR oh-my-zsh INSTALLATION
export ZSH=/home/ghost/.oh-my-zsh

# ZSH_THEME
ZSH_THEME="agnoster"

# PLUGINS
# PATH CUSTOM PLUGINS: ~/.oh-my-zsh/custom/plugins/
plugins=(git zsh-syntax-highlighting)

# RELOAD CONFIG
source $ZSH/oh-my-zsh.sh

# SYNTAX-HIGHLIGHTING
#source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
#setopt nohashdirs
#setopt completealiases
#setopt INC_APPEND_HISTORY
#setopt HIST_IGNORE_ALL_DUPS
#setopt HIST_IGNORE_DUPS
#setopt HIST_IGNORE_SPACE
#setopt HIST_EXPIRE_DUPS_FIRST
#setopt HIST_REDUCE_BLANKS
#setopt HIST_VERIFY

# MY ALIASES
alias pac="sudo pacman -S"
alias psyu="sudo pacman -Syyu --noconfirm"
alias pacr="sudo pacman -Rnsc"
alias paco="sudo pacman -Sc && sudo pacman-optimize"
alias pacsearch="pacman -Sl | cut -d' ' -f2 | grep "
alias cleaning="sudo rm -rf /var/cache/pacman/pkg/*.*"
alias weather="curl http://wttr.in/itabira"
alias sf="screenfetch | lolcat"
alias nf="neofetch --w3m ~/Imagens/logos/razer1.png --size 331px --loop --colors 7 2 7 2"
alias infosystem="~/Documentos/info-i3.sh"
alias q="exit"

# PYWAL
#export PATH="${PATH}:${HOME}/.local/bin/"
#cat ~/.cache/wal/sequences
