#!/bin/bash

# dossier source
src_dir="/home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/exercice2/dossier_a_backup"

# dossier de destination
dest_dir="/home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/dossier_dest_backup"

# copie des fichiers avce l'outil "cp"
cp -r $src_dir/* $dest_dir/