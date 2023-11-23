liste = [1, 2, 3, 4, 5]

def fliste(liste):
    print(liste)
    liste[0], liste[-1] = liste[-1], liste[0]
    print(liste)

fliste(liste)