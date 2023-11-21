"""
    Traitement de l'affichage : 
    une version avec turtle pour un affichage tres precis, construit au fur et a mesure
    et une version manipulant des fonctions de la bibliotheque matplotlib.pyplot pour un affichage imediat
"""

from lecture import *
from methode_incomplete import *
from turtle import *
import matplotlib.pyplot as plt
import numpy as np 

def affichage_matrice(matrice,N,M):
    """
        Fonction d'affichage d'une matrice NxM sur le terminal.
        Utilisee pour debogage et tests.
    """

    for i in range(N):
        for j in range(M):
            if matrice[i][j]==BLANC:
                print(" ",end="")
            elif matrice[i][j] == VIDE:
                print("|?|",end="")
            elif matrice[i][j]==NOIR:
                print("|x|",end="")
        print("\n")
    print("\n")


def initier_turtle():
    """Fontion d'initialisation pour le premier type d'affichage."""

    global coloriage 
    coloriage = Turtle()
    coloriage.speed(speed=0)
    coloriage.shapesize(stretch_wid=0.001, stretch_len=0.001, outline=0.008) 
    return coloriage

def tracer_case(t,x,y,size,fill_color):
    """Fonction pour tracer un carre pour le premier type d'affichage."""

    t.penup()
    t.goto(x,y)
    t.pendown() 
    t.fillcolor(fill_color)
    t.begin_fill()

    for _ in range(0,4):
        coloriage.forward(size)
        coloriage.right(90)

    t.end_fill()


def tracer_grille(grille):
    """Fonction pour tracer et afficher une grille pour le permier type d'affichage."""

    square_color = "black"
    start_x = -window_width()//2
    start_y = window_height()//2
    box_size = 10 
    for i in range(0,grille.N):
        for j in range(0,grille.M):
            square_color = 'black' if grille.matrice[i][j] == NOIR else 'white'
            tracer_case(coloriage,start_x+j*box_size,start_y-i*box_size,box_size,square_color)


def afficher_grille(grille):
    """Fontion pour afficher une grille pour le deuxieme type d'affichage."""

    # creation de l'image
    figure = plt.figure()

    # parametres d'affichage
    axe = figure.add_subplot(1, 1, (1,1))

    minor_ticks = np.arange(0, grille.N, 1)
    major_ticks = np.arange(0, grille.M, 1)

    axe.set_xticks(minor_ticks, minor=True)
    axe.set_yticks(minor_ticks, minor=True)

    axe.set_xticks(major_ticks)
    axe.set_yticks(major_ticks)

    axe.grid(which='both')
    axe.set_xticklabels([])
    axe.set_yticklabels([])

    # affichage de la grille
    for i in range(grille.N) :
        for j in range(grille.M) :

            if grille.matrice[i][j] == BLANC :
                plt.fill_between([j, j + 1], i, i + 1, color = 'white')

            elif grille.matrice[i][j] == NOIR:
                plt.fill_between([j, j + 1], i, i + 1, color = 'black')

            else:
                plt.fill_between([j, j + 1], i, i + 1, color = 'gray')

    # ajuster l'image (axes et echelle)
    plt.gca().invert_yaxis() 
    plt.axis('scaled') 
    plt.show()
