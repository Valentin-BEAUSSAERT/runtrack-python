texttest=input("Veuillez renseignez une phrase ou un mot \n")
nbe=0

for lettre in texttest:
    if lettre == "e":
        nbe += 1

if nbe >= 1 : 
    print("Cette chaîne de caractère contient " + str(nbe) + " lettre e")
else : print("Cette chaîne de caractère ne contient pas de lettre e")
