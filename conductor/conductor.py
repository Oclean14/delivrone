from tkinter import *
import math, random
import sqlite3

# Fenetre
LARGEUR = 480
HAUTEUR = 320

# Drone
RAYON = 5  # rayon des drones
NUMBER_DRONE = 10

# Station
COTE = 5
NUMBER_STATION = 5


# direction initiale alatoire
vitesse = random.uniform(1.8, 2) * 5
angle = random.uniform(0, 2 * math.pi)
DX = vitesse * math.cos(angle)
DY = vitesse * math.sin(angle)

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
def bddCreation():
    """
    CREATE TYPE droneStatus AS ENUM('busy','free','maintenance');
       
    CREATE TYPE stationStatus AS ENUM('working','empty');
        
    CREATE TYPE deliveryStatus AS ENUM('not assigned','in progress','cancelled'); """

    conn.commit()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS drone(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         status TEXT
    )
    """)

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS station(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            status TEXT,
            xCoord FLOAT,
            yCoord FLOAT,
            batterieNumber INTEGER ,
            anticipatedBatterieNumber INTEGER
       )
       """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mission(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             status TEXT
             xStockCoord FLOAT,
             yStockCoord FLOAT,
             xFinalCoord FLOAT,
             yFinalCoord FLOAT,
             creationDate DATETIME
        )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mission_drone(
             drone_id INTEGER,
             mission_id INTEGER,
             FOREIGN KEY(drone_id) REFERENCES drone(id),
             FOREIGN KEY(mission_id) REFERENCES mission(id)
        )
        """)
    conn.commit()


def random2DCoords():
    return [random.uniform(RAYON/2,LARGEUR-RAYON/2),random.uniform(RAYON/2,HAUTEUR-RAYON/2)]


def createDrones(number):
    i = 1
    while i < number:
        cursor.execute("""
        INSERT INTO drone(status) VALUES("free")""" )
        i = i+1
    conn.commit()


def deplacement():
    """ Dplacement de la balle """
    global X, Y, DX, DY, RAYON, LARGEUR, HAUTEUR

    # rebond  droite
    if X + RAYON + DX > LARGEUR:
        X = 2 * (LARGEUR - RAYON) - X
        DX = -DX

    # rebond  gauche
    if X - RAYON + DX < 0:
        X = 2 * RAYON - X
        DX = -DX

    # rebond en bas
    if Y + RAYON + DY > HAUTEUR:
        Y = 2 * (HAUTEUR - RAYON) - Y
        DY = -DY

    # rebond en haut
    if Y - RAYON + DY < 0:
        Y = 2 * RAYON - Y
        DY = -DY

    X = X + DX
    Y = Y + DY

    # affichage
    Canevas.coords(Balle, X - RAYON, Y - RAYON, X + RAYON, Y + RAYON)

    # mise  jour toutes les 50 ms
    Mafenetre.after(50, deplacement)


# Cration de la fentre principale
Mafenetre = Tk()
Mafenetre.title("Animation Balle")

# Cration d'un widget Canvas
Canevas = Canvas(Mafenetre, height=HAUTEUR, width=LARGEUR, bg='white')
Canevas.pack(padx=15, pady=15)
bddCreation()
createDrones(5)
# Cration d'un objet graphique
Balle = Canevas.create_oval(X - RAYON, Y - RAYON, X + RAYON, Y + RAYON, width=1, fill='green')

deplacement()
Mafenetre.mainloop()
conn.close()