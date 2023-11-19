"""
    Deuxieme partie : Methode complete de resolution
"""

from lecture import *
from methode_incomplete import *
from math import *


#Question 13

def Enumeration(G,seq_lignes,seq_colonnes) :
    """
        Fontion de resolution complete de l'instance.
        Elle indique si la resolution de l'instance est possible ou non et retourne la matrice coloriee completement.
        
    """
    
    # dimensions de la matrice (grille)
    N = len(G)
    M = len(G[0])
    
    # algorithme de propagation
    (ok, new_G_mat) = ColoreGrille(G,seq_lignes,seq_colonnes)
    
    # le puzzle n'a pas de solution
    if ok == FAUX :
        V = [[VIDE for _ in range(M)] for _ in range(N)]
        return (FAUX,V)
    
    else :

        # premiere case indeterminee (==VIDE)
        k = CaseIndeterminee(new_G_mat,0)
        
        # appel recursif avec l'hyp que la case coloriee en blanc
        (ok1, new_G_mat1) = EnumRec(new_G_mat,k,BLANC,seq_lignes,seq_colonnes) 
        if ok1 == VRAI :
            return (ok1, new_G_mat1)
        
        # car la fonction ne retourne rien si on met en or
        # appel recursif avec l'hyp que la case est coloriee en noir
        (ok2,new_G_mat2) = EnumRec(new_G_mat,k,NOIR,seq_lignes,seq_colonnes)
        if ok2 == VRAI :
            return (ok2, new_G_mat2)

    if ok1 == FAUX and ok2 == FAUX :
        # incoherence, car la case ne peut etre ni blanche, ni noire
        V = [[VIDE for _ in range(M)] for _ in range(G.N)]
        return (FAUX,V)
    else :
        print("Erreur : ok1 = "+str(ok1)+" et ok 2 = "+str(ok2))


def EnumRec(G,k,c,seq_lignes,seq_colonnes):
    """Fonction qui code l'algorithme recursif d'enumeration.
    Elle indique si la resolution de l'instance est possible ou non et retourne la matrice coloriee.
    La resolution se fait a partir de la permiere case non coloriee."""

    # dimensions de la matrice
    N = len(G)
    M = len(G[0])
    if k == N*M :
        return (VRAI,G)
    
    i = floor(k/M) 
    j = k%M
    (ok, new_G) = ColorierEtPropager(G,i,j,c,seq_lignes,seq_colonnes)
    
    if ok == FAUX :
        
        V = [[VIDE for _ in range(M)] for _ in range(N)]
        return (FAUX,V)
    elif ok == VRAI :
        
        return (VRAI,new_G)
    else :
        # on avance a la prochaine case indeterminee
        new_k = CaseIndeterminee(G,k+1)
        (ok1, new_G_mat1) = EnumRec(new_G,new_k,BLANC,seq_lignes,seq_colonnes)
        if ok1 == VRAI :
            return (ok1, new_G_mat1)

        
        (ok2,new_G_mat2) = EnumRec(new_G,new_k,NOIR,seq_lignes,seq_colonnes)
        if ok2 == VRAI :
            return (ok2, new_G_mat2)

    if ok1 == FAUX and ok2 == FAUX :
        # incoherence
        V = [[VIDE for _ in range(M)] for _ in range(N)]
        return (FAUX,V)
    else :
        print("Erreur : ok1 = "+str(ok1)+" et ok 2 = "+str(ok2))


def ColorierEtPropager(G, i, j, c, seq_lignes, seq_colonnes) :
    """
        Fonction qui code l'algorithme de propagation pour le coloriage d'une grille en commencant par colorier la case (i,j) par la couleuur c.
        Elle indique si la resolution de l'instance est possible ou non et retourne la matrice coloriee completement ou partiellement.
        Hypothese : la matrice G est partiellement coloriee en entree.
    """
    
    # une structure tres proche de ColoreGrille (la methode partielle de resolution)
    newG = deepcopy(G)
    # dimensions de la matrice(grille)
    N = len(seq_lignes)
    M = len(seq_colonnes)
    
    # listes de lines et colonnes a voir : au debut de l'algorithme, on doit voir i et j
    LignesAVoir = [i]
    ColonnesAVoir = [j]


    # on commence par colorier la case (i,j) par la couleur c (parametres)
    newG[i][j] = c
    
    while (LignesAVoir != [] or ColonnesAVoir != []) :
        
        # on essaye de colorier les lignes
        for i in LignesAVoir :
            
            # liste des nouvelles colonnes a voir et a rajouter a ColonnesAVoir
            nouveaux_col = []
            (ok,newG)= ColoreLig(newG, M, seq_lignes, i, nouveaux_col)
            
            # ajout des colonnes
            for x in nouveaux_col :
                if x not in ColonnesAVoir :
                    ColonnesAVoir.append(x)

            LignesAVoir.remove(i)

            # le puzzle n'a pas de solution
            if ok == FAUX : 
                # incoherence trouvee 
                return (FAUX,newG)

        # on essaye de colorier les colonnes
        for j in ColonnesAVoir :

            # liste des nouvelles lignes a voir et a rajouter a LignesAVoir
            nouveaux_lig = []
            (ok, newG) = ColoreCol(newG, N, seq_colonnes, j, nouveaux_lig)

            # ajout des lignes
            for x in nouveaux_lig :
                if x not in LignesAVoir :
                    LignesAVoir.append(x)

            ColonnesAVoir.remove(j)

            # le puzzle n'a pas de solution
            if ok == FAUX : 
                # incoherence trouvee 
                return (FAUX,newG)

    # on teste si la grille est entierement coloriee
    for a in range(N) :
        for b in range(M) :
                if (newG[a][b]==VIDE):
                    return (NESAISPAS,newG)

    return (VRAI,newG)


def CaseIndeterminee(G_mat,k):
    """Fonction qui determine la premiere case vide de la grille."""

    # on determine les dimensions de la matrice et l'intervalle 
    N = len(G_mat)
    M = len(G_mat[0])
    a = floor(k/M)
    b = k%M
    
    # on verifice les cases 
    for i in range(a,N) :
        for j in range(b,M):
            if G_mat[i][j] == VIDE :
                return M*i + j
            
    # cas si aucune case est vide
    return M*N



