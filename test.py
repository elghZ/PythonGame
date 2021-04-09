from tkinter import *

#Une fonction pour le deplacement :

def deplacement():
    global dx, dy
    #On deplace l'image :
    canvas.move(W_image,dx,dy)
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


#Déplacement de l'image au départ:
dx=0
dy=0

#On cree une fenêtre et un canevas:
tk = Tk()

#chemin d'acces a l'image:
imgfile = 'pacman.gif'
# Utilisation d'un dictionnaire pour conserver une reference:
gifsdict={}

#Creation de l'image:
img = PhotoImage(file = imgfile)
gifsdict[imgfile] = img

canvas = Canvas(tk,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)
 
#Création  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()
 
#l'image réduite:
img_2 = img.subsample(10, 10)

#On cree le Widget image dans le canvas:
#NW=Nord West, le coin haut guche de l'image sera positionne a (10,10):
W_image=canvas.create_image(250,200,anchor=NW,image=img_2)

#On associe chaque touche à ca fonction
canvas.bind_all('<Right>', droite)
canvas.bind_all('<Left>', gauche)
canvas.bind_all('<Up>', haut)
canvas.bind_all('<Down>', bas)

deplacement()
 
#On lance la boucle principale:
tk.mainloop()