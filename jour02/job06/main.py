# Programme pour afficher les nombres premiers jusqu'à 1000 sans utiliser de fonction

i = 2  # Commencer à vérifier à partir de 2

while i <= 1000:
    # Supposer que le nombre est premier
    ipremier = True

    # Vérifier si le nombre est divisible par un autre nombre
    for j in range(2, i):
        if i % j == 0:
            ipremier = False
            break

    # Si le nombre est premier, l'afficher
    if ipremier:
        print(i)

    # Passer au nombre suivant
    i += 1