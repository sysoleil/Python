print ("argonaute")
print ("Hissons nos voiles avec enthousiasme et courage vers Colchide")
print ("Allons récupérer la toison d'or des griffes du dragon ")
print("Nous gagnerons, avec ou sans sandales.")
quantiteEauBu=390
print("la quantité d'eau consommée depuis le début du voyage est", quantiteEauBu,"litres")
#Calculate nb of days left

water=1000
consumed=390
left=water-consumed
leftPerArgonaute=left/50
NbDay=leftPerArgonaute/2

print("We drank",consumed, "liter of water")
print("there is",left, "liter of water left")
print("we can survive another",NbDay)

# a condition in Python
import random
#L'instruction random.randint(1, 2) va générer un nombre aléatoire soit 1, soit 2 

DiceValue=random.randint(1,2)
if DiceValue==1:
  print("Argonautes, votre voyage durera encore 10 jours")
else :
    print("Argonautes, direction le tourbillon")

#champ=4000
#taureau=200
#NbTour=champ/taureau
NbTour=20
for NbTour in range(1,21):
  print("Tour", NbTour," ok")