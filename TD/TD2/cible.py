import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Cible")
canvas_size = 600

canvasB=tk.Canvas(height=600,width=600,bg="black")

nb_cercle = 30
epaisseur = (canvas_size//2)//nb_cercle

l_couleur = ["blue","green","black","yellow","magenta","red"]

for i in range(nb_cercle,0,-1):
        canvasB.create_oval((canvas_size//2)+i*epaisseur,
                            (canvas_size//2)+i*epaisseur,
                            (canvas_size//2)-i*epaisseur,
                            (canvas_size//2)-i*epaisseur,fill=l_couleur[-i%len(l_couleur)])
canvasB.grid(row=1, column = 1)

fenetre.mainloop()