# PATH TO YOUR OH-MY-ZSH INSTALLATION
export ZSH=~/.oh-my-zsh

# ZSH_THEME
ZSH_THEME="spaceship"

# PLUGINS
# PATH CUSTOM PLUGINS: ~/.oh-my-zsh/custom/plugins
plugins=(git zsh-syntax-highlighting zsh-autosuggestions)

# RELOAD CONFIG
source $ZSH/oh-my-zsh.sh

# SPACESHIP
SPACESHIP_PROMPT_ORDER=(
  user          # Username section
  dir           # Current directory section
  host          # Hostname section
  git           # Git section (git_branch + git_status)
  hg            # Mercurial section (hg_branch  + hg_status)
  exec_time     # Execution time
  line_sep      # Line break
  vi_mode       # Vi-mode indicator
  jobs          # Background jobs indicator
  exit_code     # Exit code section
  char          # Prompt character
)

SPACESHIP_USER_SHOW=always
SPACESHIP_PROMPT_ADD_NEWLINE=true
SPACESHIP_CHAR_SYMBOL="❯"
SPACESHIP_CHAR_SUFFIX=" "

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

# YARN
export PATH=$PATH:$(yarn global bin)

# ANDROID STUDIO
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk
export ANDROID_HOME=~/.Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:~/.android-studio/bin

# FLUTTER
export PATH=$PATH:$HOME/.flutter-dev/flutter/bin
