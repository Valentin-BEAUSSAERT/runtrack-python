#Définition de la fonction avec un paramètre
def time_text(temps):
    heures = temps // 60  #Définition de la variable heures qui est égal au paramètre divisé par 60 (car il y a 60 minutes dans 1h)
    minutes = temps % 60  #Définition de la variable qui est égal au reste de la division 
    print(f"{heures} heure(s) et {minutes} minute(s)") #Imprime la conversion du chiffre en heures et minutes

#Appel de la fonction 
time_text(60)
time_text(160)
time_text(3090)