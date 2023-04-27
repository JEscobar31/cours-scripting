#!/bin/bash

#declaration des arguments
nb1=$1
nb2=$2

#stock l'addition des deux nombres avant comparaison
result=$(($nb1 + $nb2))

# Condition 
if [ $result -lt 100 ]; 
then
  echo "less_than_100 #antonio est trop bete"
else
  echo "more_or_equal_than_100"
fi