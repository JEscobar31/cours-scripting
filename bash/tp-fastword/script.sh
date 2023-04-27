#!/bin/bash

mot=$(shuf -n1 dico.txt)

nb_mots_corrects=0
while [ $nb_mots_corrects -lt 10 ]
do
  echo "Nouveau mot : $mot"
  
  read reponse
  
  if [ "$reponse" == "$mot" ]
  then
    echo "Bravo !"
    nb_mots_corrects=$(($nb_mots_corrects+1))
    mot=$(shuf -n1 dico.txt) 
  else
    echo "Erreur : $mot"
  fi
done

# Affichage du temps d'exécution
echo "Temps d'exécution :"
