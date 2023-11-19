"""
    Lecture des instances et affichage sur le terminal
"""

import re

# Variables constantes qui representent les couleurs
VIDE = 0
BLANC = 1
NOIR = 2

# Variables constates qui representent la resolution du probleme
FAUX = 0
VRAI = 1
NESAISPAS = -1


class Instance:
    """Classe representant une instance d'un probleme de tomographie discrete."""

    def __init__(self, nom_fichier):
        tab_lignes, N, tab_colonnes, M = read_file(nom_fichier)
        self.tab_lignes = tab_lignes
        self.tab_colonnes = tab_colonnes
        self.N = N
        self.M = M

    def __str__(self):
        return f"{self.N}{self.tab_lignes}{self.M}{self.tab_colonnes}"


class Grille:
    """Classe representant une grille associee a une instance de probleme."""

    def __init__(self, N, M):
        self.matrice = [[VIDE for _ in range(M)] for _ in range(N)]
        self.N = N
        self.M = M

    def __str__(self):
        return f"({self.N}x{self.M}){self.matrice}"


def read_file(path):
    """Fontion de lecture d'un fichier representant une instance de probleme."""

    tab_colonnes = []
    tab_lignes = []
    f = open(path, 'r')
    for line in f:
        if line.startswith("#"):
            break
        for num in line.split(' '):
            if num == '\n':
                if line == '\n':
                    tab_lignes.append([])
            else:
                tab_lignes.append(
                    [int(num) for num in line.split(' ') if num != '\n'])
                break
    for line in f:
        for num in line.split(' '):
            if num == '\n':
                if line == '\n':
                    tab_colonnes.append([])
            else:
                tab_colonnes.append(
                    [int(num) for num in line.split(' ') if num != '\n'])
                break
    return tab_lignes, len(tab_lignes), tab_colonnes, len(tab_colonnes)
