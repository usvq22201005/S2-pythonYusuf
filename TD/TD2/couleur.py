import tkinter as tk
from random import randint

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i,j,color):
    canvasB.create_rectangle(i,j,i+1,j+1, fill=color)

def aleatoire():
    for i in range(0,256):
        for j in range(0,256):
            color1 = get_color(r,randint(0,255),randint(0,255))
            draw_pixel(i,j,color1)

    



fenetre = tk.Tk()
fenetre.title("Couleur")

canvasB=tk.Canvas(height=256,width=256,bg="black",highlightbackground="grey",highlightthickness=3)
boutton_aleatoire = tk.Button(text="Aléatoire", command=aleatoire)
boutton_degrade = tk.Button(text="Dégradé Gris")
boutton_degrade2D = tk.Button(text="Dégradé 2D")

canvasB.grid(row=1, column = 1, rowspan= 3)
boutton_aleatoire.grid(row = 1, column= 0)
boutton_degrade.grid(row = 2, column= 0)
boutton_degrade2D.grid(row = 3, column= 0)

fenetre.mainloop()