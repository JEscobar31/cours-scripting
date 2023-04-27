#!/bin/bash

#création des arguments
victoire=$1
defaite=$2
egalite=$3

score-equipe=$(($victoire*3+egalite+defaite*(-1)))

echo $victoire
echo $defaite
echo $egalite