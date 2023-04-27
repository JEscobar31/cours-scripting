#!/bin/bash

# Définition des tableaux d'efficacité
declare -A efficacite
efficacite["feu","plante"]="super efficace !"
efficacite["feu","eau"]="ce n'est pas efficace"
efficacite["plante","eau"]="super efficace !"
efficacite["plante","feu"]="ce n'est pas efficace"
efficacite["eau","feu"]="super efficace !"
efficacite["eau","plante"]="ce n'est pas efficace"

# Vérification des types et renvoi du résultat
if [[ "${efficacite[$1,$2]}" ]]; then
  echo "${efficacite[$1,$2]}"
else
  echo "Types de Pokémon non reconnus"
fi*