liste = [4, 8, 5, 2, 1, 9, 7, 3, 6]         #Défini la liste

def fliste(liste):                  #Défini la fonction fliste prenant comme paramètre "liste"
    n = 0               #Défini la variable n pour compter le nombre de chiffre dans la liste
    for chiffre in liste:               #Pour chaque argument dans la liste :
        n += 1                          #le compteur gagne +1

    for i in range(n):              #Boucle qui s'exécute n fois où n est la longueur de la liste
        for j in range(0, n-i-1):       #Parcourt la liste de l'indice 0 jusqu'à n-i-1
            if liste[j] > liste[j+1]:        #Compare l'élément courant liste[j] avec l'élément suivant liste[j+1]
                liste[j], liste[j+1] = liste[j+1], liste[j]         #échange entre les deux éléments si la condition précédente est vraie

    return liste

fliste(liste)
print(fliste(liste))

    
    

