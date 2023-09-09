from tkinter import *
from form_finance import facture
from list_finc import list_finc
class finance:
    def __init__(self, root, width, height):
        root.delete(all)
        #partie bouton
        
        self.bouton=Canvas(root, width=width, height=60, bg="gray8")
        self.bouton.place(x=0,y=0)
        
        #Ajouer une facture
        
        Button(self.bouton, text="     Ajouter     ", bg="blue2", fg="white", font=("Arial 15"),
               command= lambda: facture(self.corp)
               ).place(x=300, y=20)
        
        #List des depenses 
        Button(self.bouton, text="     Listes     ", bg="blue2", fg="white", font=("Arial 15"),
               command= lambda: list_finc(self.corp)
               ).place(x=500, y=20)
        
        #corps
        
        self.corp=Canvas(root, width=width, height=height-60, bg="light cyan")
        self.corp.place(x=0, y=60)