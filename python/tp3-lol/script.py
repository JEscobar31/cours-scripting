conso_gragas_horaire = 1
conso_ornn_horaire = conso_gragas_horaire / 3 

conso_olaf_horaire = conso_gragas_horaire + conso_ornn_horaire + 

print(conso_totale_horaire)
temps_conso_1_bidon = 60 / conso_totale_horaire

if temps_conso_1_bidon > 42:
    print("le chellenge est raté")
else:
    print("le challenge est réussie en ")
    print(temps_conso_1_bidon)