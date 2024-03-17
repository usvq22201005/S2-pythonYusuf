import tkinter as tk
from random import randint


def couleure():
    global couleur
    couleur = input("Choisissez une couleur en anglais")
    return couleur

def dessine_carre():
    centre_y = randint(50, Canvas_height - 50)
    centre_x = randint(50, Canvas_width - 50)
    canvasB.create_rectangle(centre_x-50, centre_y-50, centre_x + 50, centre_y + 50, fill=couleur)

def dessine_croix():
    centre_y = randint(50, Canvas_height - 50)
    centre_x = randint(50, Canvas_width - 50)
    canvasB.create_line(centre_x, centre_y - 50, centre_x, centre_y + 50, fill = couleur)
    canvasB.create_line(centre_x - 50, centre_y, centre_x + 50, centre_y, fill = couleur)

def dessine_disque():
    centre_y = randint(50, Canvas_height - 50)
    centre_x = randint(50, Canvas_width - 50)
    canvasB.create_oval(centre_x-50, centre_y-50, centre_x + 50, centre_y + 50, fill=couleur)

        

couleur = "blue"
    
Canvas_height = 600
Canvas_width = 500

fenetre = tk.Tk()
fenetre.title("Mon Dessin")

canvasB=tk.Canvas(height=600,width=600,bg="black")
button_cercle=tk.Button(text="Cercle", command=dessine_disque)
button_carre=tk.Button(text="Carré", command=dessine_carre)
button_croix=tk.Button(text="Croix", command=dessine_croix)
button_couleur=tk.Button(text="Choisir une couleur", command=couleure)

canvasB.grid(row=1, column = 1, rowspan= 3)
button_couleur.grid(row=0, column=1)
button_cercle.grid(row=2,column=0)
button_carre.grid(row=3,column=0)
button_croix.grid(row=1, column=0)

fenetre.mainloop()