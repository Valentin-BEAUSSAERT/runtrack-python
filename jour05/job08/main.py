def my_sort(t): #Tri à sélection d'une liste "t"
    n = len(t)
    a = 0 #nombre de tour nécéssaire aux boucle pour trié la liste 
    for i in range(0,n-1):
        min = i #Conserver la valeur minimal
        for j in range(i+1,n):
            if t[j] < t[min]:
                min = j #Actualiser la valeur minimal
            if min != i :
                t[i] , t[min] = t[min], t[i] #remplace les valeurs
    a = i + j
    print("Liste trié :",t,"Nombre de coup total :",a)

my_sort([7, 11, 42, 39, 2])
my_sort([7, 11, 42, 39, 2,15,40,32,85,4,1])