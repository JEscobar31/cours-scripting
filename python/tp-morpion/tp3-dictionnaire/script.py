bulletin = {'toto': 12, 'tutu': 11, 'titi': 10, 'tata': 9}

# Initialisation des variables pour stocker le nom de l'élève ayant la note la plus basse et la plus élevée
eleve_min = " "
note_min = 0
eleve_max = " "
note_max = 20

# Parcours du dictionnaire pour trouver l'élève avec la note la plus basse et la plus élevée
for eleve, bulletin in bulletin.items():
    if bulletin < note_min:
        eleve_min = eleve
        note_min = bulletin
    if bulletin > note_max:
        eleve_max = eleve
        note_max = bulletin

# Affichage des noms des élèves ayant la note la plus basse et la plus élevée
print("L'élève qui a majoré est :", eleve_max)
print("L'élève qui a minoré est :", eleve_min)

        


