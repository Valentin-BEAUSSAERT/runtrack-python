def verif(nombre):
    if type(nombre) != int or nombre < 0:
        print("Le nombre n'est pas positif ou un entier ")
    else:
        if nombre%2 == 0:
            print ("Le nombre est pair")
        else:
            print ("Le nombre est impair")

verif(10)
verif(9)
verif(8.5)
verif(-5)

 
    
    