#Définition de la fonction 
def dev(langage):
    if langage == "JavaScript":  #Début de la boucle if qui stipule que si le paramètre de la fonction est JavaScript alors il imprime tu es un développeur web 
        print("Tu es un développeur web")
    elif langage == "Python":          #Sinon si c'est Python il imprime tu es un développeur IA
        print("Tu es un développeur IA")
    elif langage == "java":             #Sinon si c'est Java il imprime tu es un développeur logiciel
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":          #Sinon si c'est reactjs tu imprime Tu es un développeur mobile
        print("Tu es un développeur mobile")
    else:                           #Sinon tu imprimes Un jour, je serai le meilleur développeur
        print("Un jour, je serai le meilleur développeur")

#Appel de la fonction 
dev("JavaScript")
dev("Python")
dev("java")
dev("reactjs")
dev("none")