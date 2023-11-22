def dev(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    if type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    if type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    if type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")

dev("fruits", "hiver")
dev("fruits", "ete")
dev("legume", "hiver")
dev("legume", "ete")
