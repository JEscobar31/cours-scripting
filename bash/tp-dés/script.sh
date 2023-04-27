#!/bin/bash

# Récupère le nombre de lancés à effectuer
nblance=$1
score=0

for ((i=1; i<=$nblance; i++)); do
  de1=$((RANDOM % 20 + 1))
  de2=$((RANDOM % 20 + 1))

  score=$((score + de1 + de2))

  if [ $de1 -eq $de2 ]; then
    echo "Mort"
    exit 0
  fi
done

echo "Score final: $score"