#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <nom de la musique>"
  exit 1
fi

yt-dlp "ytsearch1:$1" --audio-format mp3 --output "%(title)s.%(ext)s"
