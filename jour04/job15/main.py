def custom_round(number):
    """
    Arrondit un nombre sans utiliser la fonction round().
    """
    integer_part = int(number)  # Obtient la partie entière du nombre
    decimal_part = number - integer_part  # Calcule la partie décimale
    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part

def custom_sort(list_to_sort):
   
    n = 0  # Calcul de la longueur de la liste sans utiliser len()
    for item in list_to_sort:
        n += 1

    # Tri à bulles
    for i in range(n):
        for j in range(0, n-i-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]

    return list_to_sort

# Liste d'exemple
exemple_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres de la liste et les trier
arrondi_et_trie = custom_sort([custom_round(num) for num in exemple_liste])
print (arrondi_et_trie)