#!/bin/sh

MPD_MUSIC_PATH="/home/$USER/Music"
TMP_COVER_PATH="/tmp/mpd-track-cover"

exiftool -b -Picture "$MPD_MUSIC_PATH/$(mpc --format "%file%" current)" > "$TMP_COVER_PATH"
