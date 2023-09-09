from tkinter import *
from form_rdv import rdv
from list_rdv import list_rdv
class rendez_vous:
    def __init__(self, root, width, height):
        root.delete(all)
        #partie bouton
        
        self.bouton=Canvas(root, width=width, height=60, bg="gray8")
        self.bouton.place(x=0,y=0)
        
        #Ajouer un rdv
        
        Button(self.bouton, text="     Ajouter     ", bg="blue2", fg="white", font=("Arial 15"),
               command= lambda: rdv(self.corp)
               ).place(x=300, y=20)
        
        #List des rdv 
        Button(self.bouton, text="     Listes     ", bg="blue2", fg="white", font=("Arial 15"),
               command=lambda: list_rdv(self.corp)
               ).place(x=500, y=20)
        
        #corps
        
        self.corp=Canvas(root, width=width, height=height-60, bg="light cyan")
        self.corp.place(x=0, y=60)