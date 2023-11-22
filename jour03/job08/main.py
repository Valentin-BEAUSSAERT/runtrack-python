#Définition de la fonction avec 2 paramètres
def dev(type, saison):
    if type == "fruits" and saison == "hiver":  #Début de la boucle if qui stipule que si les paramètre sont fruits et hiver alors il imprime orange, mandarine et kiwi
        print("orange, mandarine et kiwi")
    if type == "fruits" and saison == "ete":    #Idem avec fruits et ete qui imprime Poire, fraise, cassis
        print("Poire, fraise, cassis")
    if type == "legume" and saison == "hiver":  #Idem avec legume et hiver qui imprime carotte topinambour et endive
        print("carotte, topinambour, endive")
    if type == "legume" and saison == "ete":    #Idem avec legum et ete qui imprime artichaud, aubergine, navet
        print("artichaut, aubergine, navet")

#Appel de la fonction 
dev("fruits", "hiver")
dev("fruits", "ete")
dev("legume", "hiver")
dev("legume", "ete")
