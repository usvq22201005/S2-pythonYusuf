import tkinter as tk
from random import randint


def couleure():
    couleur = input("Choisissez une couleur en anglais")
    return couleur

def dessine_carre():
    carre_x = randint(0,100)
    carre_y = randint(0,100)
    canvasB.create_rectangle(carre_x-50, carre_y-50, carre_x+50, carre_y+50, fill=couleure)




fenetre = tk.Tk()
fenetre.title("Mon Dessin")

canvasB=tk.Canvas(height=600,width=600,bg="black")
button_cercle=tk.Button(text="Cercle")
button_carre=tk.Button(text="Carré", command=dessine_carre)
button_croix=tk.Button(text="Croix")
button_couleur=tk.Button(text="Choisir une couleur", command=couleure)

canvasB.grid(row=1, column = 1, rowspan= 3)
button_couleur.grid(row=0, column=1)
button_cercle.grid(row=2,column=0)
button_carre.grid(row=3,column=0)
button_croix.grid(row=1, column=0)

fenetre.mainloop()