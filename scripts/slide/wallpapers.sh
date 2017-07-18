#!/bin/bash

shopt -s nullglob
cd ~/Imagens/slide/

while true; do
	files=()
	for i in *.jpg *.png; do
		[[ -f $i ]] && files+=("$i")
	done
	range=${#files[@]}

	((range)) && feh --bg-scale "${files[RANDOM % range]}"

	sleep 0.8s
done
