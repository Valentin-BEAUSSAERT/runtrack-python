#Définition de la fonction avec 1 paramètre
def verif(nombre):
    if type(nombre) != int or nombre < 0:           #Début de la condition if qui stipule que si le type de la varaible nombre est différent d'un nombre entier ou qu'il est inférieure à zéro alors il imprime le print
        print("Le nombre n'est pas positif ou un entier ")
    else:           #Sinon 
        if nombre%2 == 0:       #Si le modulo du nombre est égal à zéro alors il imprime Le nombre est pair, sinon il imprime impair
            print ("Le nombre est pair")
        else:
            print ("Le nombre est impair")

#Appel de la fonction 
verif(10)
verif(9)
verif(8.5)
verif(-5)

 
    
    