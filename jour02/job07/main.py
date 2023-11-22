# Création de la chaîne initiale
chaine_initiale = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialisation des variables
debut = 0
fin = 1

# Boucle pour créer la pyramide
while fin <= len(chaine_initiale):
    print(chaine_initiale[debut:fin])
    fin = fin + 1