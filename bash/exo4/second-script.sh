#!/bin/bash
mkdir test_bash
cd test_bash
echo "dossier crée"

# création des fichiers textes
touch 1.txt 2.txt 3.txt 
echo "les fichiers sont crées"

#copie du dossier test_bash vers test_bash_2
cd ..
mkdir test_bash_2
cp -r ./test_bash test_bash_2
echo "le dossier test_bash est copié vers le rep test_bash_2"
