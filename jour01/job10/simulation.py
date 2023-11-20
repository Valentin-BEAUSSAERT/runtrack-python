montant_initial=1000
taux_annuel=1.20
montant_annuel=montant_initial*taux_annuel
gain=montant_annuel-montant_initial
print("Gain :"  +  str(gain))

newmontant_initial=montant_initial+5000
newtaux_annuel=taux_annuel+0.02
newmontant_annuel=newmontant_initial*newtaux_annuel
newgain=newmontant_annuel-newmontant_initial
print("New Gain :" + str(newgain))

final_montant=newmontant_initial * 0.9
final_tauxannuel=newtaux_annuel - 0.01
montant_final_annuel=final_montant*final_tauxannuel
final_gain=montant_final_annuel-final_montant
print("Gain totale :" + str(final_gain))