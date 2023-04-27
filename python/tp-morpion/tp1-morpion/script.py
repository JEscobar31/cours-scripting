grille=[
    [".","X","."],
    [".","O","."],
    [".","X","."]
]

print("MORPION")
print("_______")
for ligne in grille:
    print("|"+ligne[0]+"|"+ligne[1]+"|"+ligne[2]+"|")
    # alternative à la ligne du dessus
    # print(f"|{ligne[0]}|{ligne[1]}|{ligne[2]}|")