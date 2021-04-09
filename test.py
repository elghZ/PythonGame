from tkinter import *

#Une fonction pour le deplacement vers la droite :

def deplacement():
    global dx, dy
    if canvas.coords(point)[3]>400:
        dy=-1*dy
    #On deplace la balle :
    canvas.move(point,dx,dy)
    #On repete cette fonction
    tk.after(20,deplacement)

def droite(event):
    global dx, dy
    dx=5
    dy=0

def gauche(event):
    global dx, dy
    dx=-5
    dy=0

def haut(event):
    global dx, dy
    dx=0
    dy=-5

def bas(event):
    global dx, dy
    dx=0
    dy=5
#Coordonnées de la balleau départ:
Pos_X=60
Pos_Y=10
#Déplacement de la balle au départ:
dx=0
dy=0
#On cree une fenêtre et un canevas:
tk = Tk()
canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)
 
#Création  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()
 
#On cree un point:
point = canvas.create_rectangle(200,220,210,230,fill='red')

#On associe la touche droite du clavier a la fonction droite():
canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)

deplacement()
 
#On lance la boucle principale:
tk.mainloop()