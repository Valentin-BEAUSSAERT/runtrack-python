#Définition de fonction avec 3 paramètres
def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) /3 
note1 = int(input("Veuillez saisir la première note : ")) #Demande à l'utilisateur de rentrer une note 
note2 = int(input("Veuillez saisir la deuxième note : "))   #Demande à l'utilisateur de rentrer une note 
note3 = int(input("Veuillez saisir la troisième note : "))    #Demande à l'utilisateur de rentrer une note 
 
moyenne_etudiant = moyenne(note1, note2, note3)  #Définition de la variable

if 15 <= moyenne_etudiant <= 20: #Début de la condition if qui stipule que si la moyenne est inférieure ou égale à 20 imprime Très bon élève
    print("Très bon élève") 
if 11 <= moyenne_etudiant <= 14:  #Idem mais imprime Bon élève
    print("Bon élève")
if 8 <= moyenne_etudiant <= 10:   #Idem mais imprime élève moyen
    print("Élève moyen")
if 0 <= moyenne_etudiant <= 7:      #Idem mais imprime l'élève doit faire des efforts
    print("Élève devant faire des efforts")