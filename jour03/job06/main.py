#Définition de la fonction avec un paramètre
def plus_ou_moins(nombre):
    if nombre > 0:             #Début de la boucle if qui stipule que si le nombre est supérieure à zéro alors il imprime positif
        print("Positif")
    elif nombre < 0:           #Sinon si le nombre est inférieure à 0 alors il imprime négatif
        print("Negatif")
    else:                                   #Sinon il imprime le chiffre est égale à 0
        print("Le chiffre est égale à 0")

#Appel de la fonction 
plus_ou_moins(1)
plus_ou_moins(-1)
plus_ou_moins(0)