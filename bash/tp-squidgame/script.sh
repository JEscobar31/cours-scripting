#!/bin/bash

# initialiser les points de chaque joueur à 0
j1_points=02_points=0

# boucle pour les 6 manches
for i in {1..6}
do
    echo "Manche $i :"
    
    read -p "Joueur 1, choix 'coop' ou 'trahir': " j1_choix
    read -p "Joueur 2, choix 'coop' ou 'trahir': " j2_choix
    
    if [ "$j1_choix" == "coop" ] && [ "$j2_choix" == "coop" ]
    then
        j1_points=$((j1_points + 2))
        j2_points=$((j2_points + 2))
        echo "Les deux joueurs coopèrent. Les deux joueurs gagnent 2 pièces."
    elif [ "$j1_choix" == "coop" ] && [ "$j2_choix" == "trahir" ]
    then
        j2_points=$((j2_points + 5))
        echo "Joueur 1 coopère et Joueur 2 trahit. Joueur 2 gagne 5 pièces."
    elif [ "$j1_choix" == "trahir" ] && [ "$j2_choix" == "coop" ]
    then
        j1_points=$((j1_points + 5))
        echo "Joueur 1 trahit et Joueur 2 coopère. Joueur 1 gagne 5 pièces."
    else
        echo "Les deux joueurs trahissent. Personne ne gagne de points."
    fi
    
    echo "Points après la manche $i :"
    echo "Joueur 1 : $j1_points pièces"
    echo "Joueur 2 : $2_points pièces"
done

echo "Résultat final :"
echo "Joueur 1 : $j1_points pièces"
echo "Joueur 2 : 2_points pièces"