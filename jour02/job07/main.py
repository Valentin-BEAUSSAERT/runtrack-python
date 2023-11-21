# Création de la chaîne initiale
chaine_initiale = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialisation des variables
index = 0
niveau = 1

# Boucle pour créer la pyramide
while index + niveau <= len(chaine_initiale):
    print(chaine_initiale[index:index + niveau])
    index += niveau
    niveau += 1

