"""
    Troisieme partie : tests sur le temps de calcul
"""

from lecture import *
from methode_incomplete import *
from methode_complete import *
from affichage import *
from time import *

def calcul_temps():
    """Fonction de calcul du temps d'execution des deux methodes sur les instances donnees.
        Elle cree un fichier temps.txt qui contient le tableau des temps d'execution des differentes instances selon la methode (complete ou incomplete)"""
    
    # tableau des resulatats 
    resultats = []
    
    # on parcourt la totalite des fichier
    for i in range(0, 17):
        # nom du fichier
        path_fichier = "instances/"+str(i)+".txt"
        
        # creation de l'instance
        instance = Instance(path_fichier)
        
        # creation des grilles
        
        grille_coloree1 = Grille(instance.N, instance.M)
        # methode incomplete de resolution
        t1 = time()
        (ok1, grille_coloree1.matrice) = ColoreGrille(grille_coloree1.matrice, instance.tab_lignes, instance.tab_colonnes)
        t2 = time()
        
        grille_coloree2 = Grille(instance.N, instance.M)
        
        # methode complete de resolution
        t3 = time()
        (ok2, grille_coloree2.matrice) = Enumeration(grille_coloree2.matrice,instance.tab_lignes,instance.tab_colonnes)
        t4 = time()
        
        # on retourne les temps de calculs ainsi qu'un boolean qui nous indique si la resolution est bien reussie
        # a colorier la grille / on a trouve une incoherence / on arrive pas a conclure 
        resultats.append([ok1, t2-t1, ok2, t4-t3])

    return resultats
        
        
    
def resolution_utilisateur(option,i):
    """
        Fonction d'iteraction avec l'utilisateur.
        Elle est utiliser pour le main.py .
    """

    # lecture du fichier
    path_fichier = "instances/"+str(i)+".txt"

    # creation de l'instance
    instance = Instance(path_fichier)

    # creation de la grille
    grille = Grille(instance.N, instance.M)

    if (option == 1):
        (ok, grille.matrice) = ColoreGrille(grille.matrice, instance.tab_lignes, instance.tab_colonnes)
        print("Resultat : " + str(ok) + "\n")

    elif (option == 2):
        (ok,grille.matrice) = Enumeration(grille.matrice,instance.tab_lignes,instance.tab_colonnes)
        print("Resultat : " + str(ok) + "\n")

    grille.matrice = grille.matrice
    afficher_grille(grille)