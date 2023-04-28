#!/bin/bash

url="http://apimeme.com/?ref=apilist.fun"
page_html=$(curl -s "$url")
regex='<option value="(.*?)">(.*?)</option>'
echo "$page_html" | grep -Eo "$regex" | sed -E "s|$regex|\2|" > name_memes.txt

echo "name saved"
