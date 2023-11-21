"""
    Premiere partie : Methode incomplete de resolution
"""

from copy import *
from lecture import *


# Question 4

def valeur_T(T, sequence, j, l) :
    """
        Fonction qui retourne vrai s'il est possible de colorier, pour une ligne donnee, les j+1 premieres cases avec la sous-sequence des l premiers blocs de la ligne.
        Hypothese : le tableau T initialisé avec -1 pour toutes les cases.
    """

    # Cas parametres incompatibles
    if (j < 0) or (l < 0) : 
            return False

    # Cas valeur deja calculee
    elif (T[j][l]!=VIDE):
            return T[j][l]

    # Cas 1 : sequence vide 
    elif (l == 0) : # cas 1 
            return True

    # Cas 2a : sequence trop longue pour le nombre de cases
    elif (j < sequence[l - 1] - 1) :
            return False

    # Cas 2b : la taille de la sequence et le nombre de cases sont egaux
    elif (j == sequence[l - 1] - 1) :
            return (l == 1)

    # Cas 2c : appel recursif
    else : 
            T[j][l] = (valeur_T(T, sequence, j - 1, l)) or (valeur_T(T, sequence, j - sequence[l - 1] - 1, l - 1))
            return T[j][l]


def presenceCouleur(C,ind1,ind2,couleur):
    """Fonction qui retourne vrai si C[ind1:ind2+1] contient couleur."""  

    for i in range(ind1,ind2+1):
        if C[i] == couleur:
            return False
    return True


# Question 7 :

def valeur_T_couleur(T, sequence, j, l, C) :
    """
        Version optimisee de la fonction valeur_T qui tient compte de la coloration des cases.
        Remarque : il s'agit d'un algorithme de programmation dynamique avec memoisation.
        Hypothese : C est un tableau qui contient des informations sur les cases qui sont deja coloriees dans la ligne.
    """

    # Cas si la valeur est deja connue
    if (T[j][l] != -1) : 
        return T[j][l]

    # Cas 1 : on teste si on retrouve une case noire dans une ligne qui devrait etre entierement blanche
    # si c'est le cas, il s'agit d'une incoherence
    elif (l == 0) :
            T[j][l] = presenceCouleur(C,0,j,NOIR)
            return T[j][l]

    # Cas 2b : la taille de la sequence et le nombre de cases sont egaux
    # on aimerait avoir les j+1 cases soient entierement coloriees en noir
    # donc on veut pas trouver une case blanche avant
    elif ((j == sequence[0] - 1) and (l == 1)) :
        T[j][l] = presenceCouleur(C,0,j,BLANC)
        return T[j][l]

    # Incoherence sur les donnees en entree
    # Remarque : il est important que ce cas soit apres le cas 2b, sinon on risque de ne pas prendre en compte le cas 2b
    elif (j < 0) or (l < 0):
        return False

    # Cas 2a : on retourne faux peu importe le coloriage (si < on a faux + dans cette branche l>1)
    elif (j <= sequence[l - 1] - 1) :
        T[j][l] = False
        return T[j][l]

    # Cas 2c : le dernier bloc de longueur sl est a la fin de la ligne li, donc se termine a la case (i,j)
    elif C[j]==NOIR :
        res1 = False
    else :
        # appel recursif
        res1 = valeur_T_couleur(T, sequence, j - 1, l, C)

    if (res1 == True):
        T[j][l] = True
        return T[j][l]

    else :
        # on teste la presence d'une case blanche dans la sequence
        if not presenceCouleur(C,j-sequence[l-1]+1,j,BLANC):
            res2 = False

        # on teste si la derniere case de la sequence est noire
        elif (C[j - sequence[l - 1]] == NOIR) :
            res2 = False

        else :
            # appel recursif
            res2 = valeur_T_couleur(T, sequence, j - sequence[l - 1] - 1 , l - 1, C)

        T[j][l] = (res1 or res2)

    return T[j][l]


def ColoreLig(G, M, seq_lignes, i, nouveaux_col) :
    """
        Fonction qui colorie la ligne i d'une grille selon les sequences correspondantes. 
        Hypothese : seq_lignes est le tableau de sequences de lignes.
                    nouveaux_col est la liste des colonnes a explorer apres la coloration (totale ou partielle) de la ligne i.
    """

    # taille de la sequence pour la ligne i
    longueur = len(seq_lignes[i])

    # on travaille sur une copie de la ligne i
    C = deepcopy(G[i])

    for k in range(M):

        if (C[k] == VIDE):

            # on teste la possibilite de colorier la case en blanc
            T = [[-1 for _ in range(longueur+1)] for _ in range(M)]
            C[k] = BLANC
            est_blanc = valeur_T_couleur(T, seq_lignes[i], M - 1, longueur, C)

            # on teste la possibilite de colorier la case en noir
            T = [[-1 for _ in range(longueur+1)] for _ in range(M)]
            C[k] = NOIR
            est_noir = valeur_T_couleur(T, seq_lignes[i], M - 1, longueur, C)

            # si les deux coloriages sont valides, on ne sait pas
            if (est_noir and est_blanc) :
                C[k] = VIDE

            # si la case est forcement noir, on la colorie en noir
            elif ( not est_blanc and est_noir) :
                C[k] = NOIR
                G[i][k] = NOIR
                nouveaux_col.append(k)

            # la case est forcement blanche, on la colorie en blanc
            elif (est_blanc and not est_noir) : 
                C[k] = BLANC
                G[i][k] = BLANC
                nouveaux_col.append(k)

            # si les deux coloriages ne sont pas valides, le puzzle n'a pas de solution
            else : 
                return (FAUX, G)

    return (VRAI,G)


def ColoreCol(G, N, seq_colonnes, j, nouveaux_lig):
    """
        Fonction qui colorie la colonne j d'une grille selon les sequences correspondantes. 
        Elle reprendre le meme principe que celui de la fonction ColoreLig.
        Hypothese : seq_colonnes est le tableau de sequences de colonnes.
                    nouveaux_col est la liste des lignes a explorer apres la coloration (totale ou partielle) de la colonne j.
    """

    # taille de la sequence pour la colonne j
    longueur = len(seq_colonnes[j])

    # on transforme la colonne j en "ligne"
    C = []
    for ind in range(0,N):
        C.append(G[ind][j])

    for k in range(N):

        if (C[k] == VIDE) :

            # on teste la possibilite de colorier la case en blanc
            T = [[-1 for _ in range(longueur+1)] for _ in range(N)]
            C[k] = BLANC
            est_blanc = valeur_T_couleur(T, seq_colonnes[j], N - 1, longueur, C)

            # on teste la possibilite de colorier la case en noir
            T = [[-1 for _ in range(longueur+1)] for _ in range(N)]
            C[k] = NOIR
            est_noir = valeur_T_couleur(T, seq_colonnes[j], N - 1, longueur, C)

            # si les deux coloriages sont valides, on ne sait pas
            if (est_noir and est_blanc) :
                    C[k] = VIDE

            # si la case est forcement noir, on la colorie en noir
            elif (not est_blanc and est_noir) :
                    C[k] = NOIR
                    G[k][j] = NOIR
                    nouveaux_lig.append(k)

            # la case est forcement blanche, on la colorie en blanc
            elif (est_blanc and not est_noir) :
                    C[k] = BLANC
                    G[k][j] = BLANC
                    nouveaux_lig.append(k)

            # si les deux coloriages ne sont pas valides, le puzzle n'a pas de solution
            else : 
                return (FAUX, G)

    return (VRAI,G)


# Question 9 :

def ColoreGrille(G, seq_lignes, seq_colonnes) :
    """
        Fonction qui code l'algorithme de propagation pour le coloriage d'une grille.
        Elle indique si la resolution de l'instance est possible ou non, ou encore si on ne sais pas.
        Elle retourne egalement la matrice coloriee (completement ou partiellement).
    """

    # on travaille sur une copie de la matrice G representant la grille
    newG = deepcopy(G)

    # taille de la matrice
    N = len(seq_lignes)
    M = len(seq_colonnes)

    # listes de lines et colonnes a voir : au debut de l'algorithme, on doit tout voir
    LignesAVoir = [i for i in range(N)]
    ColonnesAVoir = [i for i in range(M)]

    while (LignesAVoir != [] or ColonnesAVoir != []) :

        # on essaye de colorier les lignes
        for i in LignesAVoir :

            # liste des nouvelles colonnes a voir et a rajouter a ColonnesAVoir
            nouveaux_col = []
            (ok,newG)= ColoreLig(newG, M, seq_lignes, i, nouveaux_col)

            # ajout des colonnes
            ColonnesAVoir.extend(x for x in nouveaux_col if x not in ColonnesAVoir)
            LignesAVoir = [x for x in LignesAVoir if (x!=i)]

            # le puzzle n'a pas de solution
            if ok == FAUX : 
                return (FAUX,newG)

        # on essaye de colorier les colonnes
        for j in ColonnesAVoir :

            # liste des nouvelles lignes a voir et a rajouter a LignesAVoir
            nouveaux_lig = []
            (ok, newG) = ColoreCol(newG, N, seq_colonnes, j, nouveaux_lig)

            # ajout des lignes
            LignesAVoir.extend(x for x in nouveaux_lig if x not in LignesAVoir)
            ColonnesAVoir = [x for x in ColonnesAVoir if (x!=j)]

            # le puzzle n'a pas de solution
            if ok == FAUX : 
                return (FAUX,newG)

    # on teste si la grille est entierement coloriee
    for i in range(N):
        for j in range(M):
            if newG[i][j] == VIDE :
                return (NESAISPAS,newG)

    return (VRAI,newG)

