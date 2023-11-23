L = [8, 24, 48, 2, 16]

def calcul(L):
    compteur = 0
    for nombre in L:
        if nombre % 3 == 0:
            compteur +=1
    return compteur

compteur_multiples = calcul(L)
print ((compteur_multiples))