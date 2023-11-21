#Demande à l'utilisateur de rentrer un chiffre
n = int(input("Veuillez saisir un entier supérieur à zéro (n)\n"))

#Pour chaque nombre i dans la séquence de 1 à N inclus, répéte les instructions suivantes :
for i in range(1, n + 1):
    print(f"Table de multiplication de {i} :")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")