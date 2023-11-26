liste = [4, 8, 5, 2, 1, 9, 7, 3, 6]         #Défini la liste

def fliste(liste):                  #Défini la fonction fliste prenant comme paramètre "liste"
    n = 0               
    #Défini la variable n pour compter le nombre de chiffre dans la liste
    for chiffre in liste:               #Pour chaque argument dans la liste :
        n += 1                          #le compteur gagne +1
    i = 0
    while i < n:            #Boucle qui s'exécute n fois où n est la longueur de la liste
        j = 0
        while j < (n-i-1):      #Parcourt la liste de l'indice 0 jusqu'à n-i-1
            if liste[j] > liste[j+1]:        #Compare l'élément courant liste[j] avec l'élément suivant liste[j+1]
                liste[j], liste[j+1] = liste[j+1], liste[j] 
            j+=1        #échange entre les deux éléments si la condition précédente est vraie
        i+=1

    return liste

fliste(liste)
print(fliste(liste))

    
    

