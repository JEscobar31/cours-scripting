import os
import shutil

# dossier source et dossier de destination
src_dir = "/home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/exercice2/dossier_a_backup"
dest_dir = "/home/jere/cours-ynov/cours-script/cours-scripting/python/tp-final-enfin/dossier_dest_backup"

# Copie des fichiers
for file_name in os.listdir(src_dir):
    full_file_name = os.path.join(src_dir, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest_dir)