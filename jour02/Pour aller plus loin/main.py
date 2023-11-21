# Demander à l'utilisateur de saisir les longueurs
a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

# Vérifier si les longueurs peuvent former un triangle
if a + b > c and a + c > b and b + c > a:
    # Le triangle peut être formé, déterminer son type

    # Vérifier si le triangle est équilatéral
    if a == b == c:
        type_triangle = "équilatéral"
    # Vérifier si le triangle est isocèle (deux côtés égaux)
    elif a == b or a == c or b == c:
        isocèle = True
    else:
        isocèle = False

    # Vérifier si le triangle est rectangle (théorème de Pythagore)
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        if isocèle:
            type_triangle = "rectangle et isocèle"
        else:
            type_triangle = "rectangle"
    elif isocèle:
        type_triangle = "isocèle"
    else:
        type_triangle = "quelconque"

    print("Ces longueurs peuvent former un triangle.")
    print(f"Le triangle est {type_triangle}.")
else:
    print("Ces longueurs ne peuvent pas former un triangle.")
