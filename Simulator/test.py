from tkinter import *

def Clic(event):
    """ Gestion de l'evenement Clic gauche sur la zone graphique """
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    # on dessine un carre
    r = 20
    Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='black',fill='green')

def Effacer():
    """ Efface la zone graphique """
    Canevas.delete(ALL)

# Creation de la fenetre principale
Mafenetre = Tk()
Mafenetre.title('Carres')

# Creation d'un widget Canvas
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
# La methode bind() permet de lier un evenement avec une fonction :
# un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur Clic()
Canevas.bind('<Button-1>', Clic)
Canevas.pack(padx =5, pady =5)

# Creation d'un widget Button (bouton Effacer)
Button(Mafenetre, text ='Effacer', command = Effacer).pack(side=LEFT,padx = 5,pady = 5)

# Creation d'un widget Button (bouton Quitter)
Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy).pack(side=LEFT,padx=5,pady=5)

Mafenetre.mainloop()