#!/bin/bash

# déclaration des arguments
url_wiki=$1
mon_mot=$2

# commande qui récupére l'url, qui va chercher sur ce lien le nombre de mot "$mon_mot" et qui va compter le nombre de fois que "$mon_mot" apparait.
mot_trouve=$(curl $1 | grep -io $2) 
echo $mot_trouve
echo "nombre de fois que le mot apparait"
echo $mot_trouve | wc -w