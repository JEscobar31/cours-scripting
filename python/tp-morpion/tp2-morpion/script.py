grille=[
    [".","X","."],
    [".","O","."],
    ["X",".","."]
]
chaine = " "
for ligne in grille:
    chaine = chaine + ligne[0] + ligne[1] + ligne[2]
print(grille)
print(chaine)