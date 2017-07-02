# -*- coding: utf-8 -*-
# script animation_balle.py
# (C) Fabrice Sincère

from tkinter import *
import math, random
#from Simulator.Drone import *
from Drone import Drone
LARGEUR = 1000
HAUTEUR = 500
RAYON = 5  # rayon de la balle
direction = [950,450,0]
drone = Drone([10,10,0], 5)
drone.setDirection(direction)


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Delivrone")

# Création d'un widget Canvas
Canevas = Canvas(Mafenetre, height=HAUTEUR, width=LARGEUR, bg='white')
Canevas.pack(padx=5, pady=5)

# Création d'un objet graphique
Balle = Canevas.create_oval(drone.position[0] - RAYON, drone.position[1]  - RAYON, drone.position[0]  + RAYON, drone.position[1] + RAYON, width=1, fill='green')

destinationDisplay = Canevas.create_oval(direction[0] - RAYON, direction[1]  - RAYON, direction[0]  + RAYON, direction[1] + RAYON, width=1, fill='blue')

i=0
if not (drone.isOnTopOfDirection() and i == 0):
    print(i)
    i = 1

    drone.start()


def motion():
    global i
    print(i)



    print("au suivant")
    # affichage
    Canevas.coords(Balle, drone.position[0] - RAYON, drone.position[1]  - RAYON, drone.position[0]  + RAYON, drone.position[1] + RAYON)

    # mise à jour toutes les 50 ms
    Mafenetre.after(50, motion)



motion()
Mafenetre.mainloop()