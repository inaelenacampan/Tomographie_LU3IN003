"""
		Fonction principale
"""

from lecture import *
from methode_incomplete import *
from methode_complete import *
from affichage import *
from tests import *
from turtle import *

print("MENU\n")
print("1 : Methode incomplete\n")
print("2 : Methode complete\n")
print("3 : Quitter")
print("\n")

print("Methode choisie : ")
methode = int(input())

if (methode != 3) :
	print("Numero du fichier .txt (contenant l'instance a resoudre) : ")
	i = int(input())

while(methode!=3 and (i>=0 and i<17)):
    resolution_utilisateur(methode,i)

    print("Methode choisie : ")
    methode = int(input())
    if methode == 3 :
        break 

    else :
        print("Numero du fichier .txt (contenant l'instance a resoudre) : ")
        i = int(input())

# tests sur le temps de calculs, pour toutes les instances, pour les deux méthodes

print("Visualisation du temps de calcul pour toutes les instances? : (0/1)")
i = int(input())

if (i==1):

    tab_temps = calcul_temps()

    f = open("temps.txt", "w")
    f.write("Numero du fichier \t Temps Methode Incomplete \t Temps Methode Complete \n")

    for i in range(len(tab_temps)):
            f.write(str(i) + "\t" + str(tab_temps[i][1]) + "\t" + str(tab_temps[i][3]) + "\n")
    f.close()

    print("Resultats dans le fichier temps.txt\n")

