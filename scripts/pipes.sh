#!/bin/bash

W=$(tput cols) H=$(tput lines)
# maximal random value + 1
M=32768

SETS=('╱╲' '/\')
COLORS=(31 32 33 34 35 36 37)

# default values
N=1
T=0
I=0.05
P=25
R=$((W * H / 4))

HELP="Usage: $(basename $0) [OPTIONS]
Animated pipes.sh terminal screensaver at an angle.
Options:
  -n [1-]     number of pipes. (Default: $N)
  -t [0-$((${#SETS[@]} - 1))]    type of pipes. (Default: $T)
  -i [float]  piping interval or maze generation interval. (Default: $I)
  -P [0-100]  probability of a turning pipe or of \\ in maze generation. (Default: $P)
  -r [LIMIT]  reset after x characters, 0 if no limit. (Default: $R)
  -R          random starting point.
  -C          no color.
  -X          maze generation.
  -h          this help message.
"

while getopts "n:t:i:P:r:RCXh" arg; do
  case $arg in
    n)
      ((N = OPTARG > 0 ? OPTARG : N))
      ;;
    t)
      ((T = (OPTARG >= 0 && OPTARG < ${#SETS[@]}) ? OPTARG : T))
      ;;
    i)
      I=$OPTARG
      ;;
    P)
      ((P = (OPTARG >= 0 && OPTARG <= 100) ? OPTARG : P))
      ;;
    r)
      ((R = OPTARG >= 0 ? OPTARG : R))
      ;;
    R)
      RNDSTART=1
      ;;
    C)
      NOCOLOR=1
      ;;
    X)
      MAZE=1
      ;;
    h)
      echo -e "$HELP"
      exit 0
      ;;
  esac
done

do_exit() {
  # Show cursor and echo stdin
  echo -ne "\e[?25h"
  stty echo
  clear
  exit 0
  }
trap do_exit INT TERM

# No echo stdin and hide the cursor
stty -echo
echo -ne "\e[?25l"

# maze geneartion
while [[ $MAZE ]] && clear; do
  [[ $NOCOLOR ]] || echo -ne "\e[1;${COLORS[${#COLORS[@]} * RANDOM / M]}m"
  for ((i = 0; i < W * H; i++ )); do
    echo -ne ${SETS[T]:100 * RANDOM / M < P:1}
  done
  read -t $I -n 1 && [[ $REPLY =~ q|Q ]] && do_exit
done

# initialze values
for ((n = 0; n < N; n++)); do
  ((X[n] = RNDSTART ? (W + 2) * RANDOM / M : W / 2))
  ((Y[n] = RNDSTART ? (H + 2) * RANDOM / M : H / 2))
  D[n]=$((4 * RANDOM / M))
  C[n]=${COLORS[${#COLORS[@]} * RANDOM / M]}
done

clear
while :; do
  for ((n = 0; n < N; n++, CC = 0)); do
    x=${X[n]} y=${Y[n]}
    d=${D[n]} c=${C[n]}

    ((d = (100 * RANDOM / M) < P ? ((d + 1) + 2 * (RANDOM % 2)) % 4 : d))
    ((e = (d + 1) % 4))

    # calculate new position
    # d'  x'  y'
    # 0: x+1 y-1
    # 1: x-1 y-1
    # 2: x-1 y+1
    # 3: x+1 y+1
    ((xn = e < 2 ? x + 1 : x - 1))
    ((yn = d < 2 ? y - 1 : y + 1))
    
    # adjust position and change color?
    ((d < 2 && y == 0)) && ((yn--, CC=1))
    ((e > 1 && x == 0)) && ((xn--, CC=1))
    ((d > 1 && y == H)) && ((yn++, CC=1))
    ((e < 2 && x == W)) && ((xn++, CC=1))
    ((CC)) && c=${COLORS[${#COLORS[@]} * RANDOM / M]}

    # warp pipe
    ((xn = (xn + W + 1) % (W + 1)))
    ((yn = (yn + H + 1) % (H + 1)))

    # calculate position in terminal
    # d'  xt   yt
    # 0: x'   y'+1
    # 1: x'+1 y'+1
    # 2: x'+1 y'
    # 3: x'   y'
    ((xt = e < 2 ? xn : xn + 1))
    ((yt = d < 2 ? yn + 1 : yn))

    echo -ne "\e[${yt};${xt}H"
    [[ $NOCOLOR ]] || echo -ne "\e[1;${c}m"
    echo -n "${SETS[T]:d%2:1}"

    X[n]=$xn Y[n]=$yn
    D[n]=$d C[n]=$c
  done
  read -t $I -n 1 && [[ $REPLY =~ q|Q ]] && do_exit
  ((R)) && ((r += N, r >= R)) && r=0 && clear
done

do_exit


