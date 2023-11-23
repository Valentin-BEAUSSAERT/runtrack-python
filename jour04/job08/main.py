L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def liste(L):
    somme_nombre_pair = 0
    for nombre in L:
        if nombre % 2 == 0:
            somme_nombre_pair += nombre
    print(f"La somme des nombres paires de cette liste est de : {somme_nombre_pair}")
    
liste(L)