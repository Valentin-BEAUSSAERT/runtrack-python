
def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) /3
note1 = int(input("Veuillez saisir la première note : "))
note2 = int(input("Veuillez saisir la deuxième note : "))
note3 = int(input("Veuillez saisir la troisième note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève") 
if 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
if 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
if 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")