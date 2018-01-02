# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
  export ZSH=/home/ghost/.oh-my-zsh

# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
#ZSH_THEME="powerlevel9k/powerlevel9k"
ZSH_THEME="agnoster"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/dsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

###SYNTAX-HIGHLIGHTING###
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
setopt nohashdirs
setopt completealiases
setopt INC_APPEND_HISTORY
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_SPACE
setopt HIST_EXPIRE_DUPS_FIRST
setopt HIST_REDUCE_BLANKS
setopt HIST_VERIFY

###MEUS ALIASES###
alias pac="sudo pacman -S"
alias psyu="sudo pacman -Syyu --noconfirm"
alias pacr="sudo pacman -Rnsc"
alias paco="sudo pacman -Sc && sudo pacman-optimize"
alias pacsearch="pacman -Sl | cut -d' ' -f2 | grep "
alias limpeza="sudo rm -rf /var/cache/pacman/pkg/*.*"
alias tempo="curl http://wttr.in/itabira"
alias sf="screenfetch | lolcat"
alias lc="colorls"
alias nf="neofetch --w3m /home/ghost/Imagens/logos/razer1.png --size 331px --loop --colors 7 2 7 2"
#alias spotify="sh /home/ghost/Downloads/Git/Spotify-AdKiller/spotify-wrapper.sh"
alias infosystem="~/Documentos/info-i3.sh"
alias q="exit"
alias msfstart="sudo /opt/metasploit/ctlscript.sh start"
alias msfrestart="sudo /opt/metasploit/ctlscript.sh restart"
alias msfstop="sudo /opt/metasploit/ctlscript.sh stop"

###ALIASES DE CORES###
alias color1="~/Downloads/Git/Color-Scripts/color-scripts/colortest"
alias color2="~/Downloads/Git/Color-Scripts/color-scripts/colorbars"
alias color3="~/Downloads/Git/Color-Scripts/color-scripts/pukeskull"
alias color4="~/Documentos/pacman+.sh"
alias pipes1="~/Downloads/Git/Color-Scripts/color-scripts/pipes2"
alias pipes2="~/Downloads/Git/Color-Scripts/color-scripts/pipes2-slim"
