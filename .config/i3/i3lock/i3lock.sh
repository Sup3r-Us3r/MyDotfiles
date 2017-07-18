#!/usr/bin/env bash
set -eu

[[ -z "$(pgrep i3lock)" ]] || exit
i3lock -i ${HOME}/.config/i3/i3lock/lock.png
