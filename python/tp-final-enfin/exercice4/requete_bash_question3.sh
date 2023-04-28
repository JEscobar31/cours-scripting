#!/bin/bash

meme_name=$(shuf -n 1 name_memes.txt)
text_top=$1
text_bottom=$2
url="http://apimeme.com/meme?meme=$meme_name&top=$text_top&bottom=$text_bottom"
curl -s -o meme.png "$url"

echo "is good"
