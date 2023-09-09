from tkinter import *
from fonctions import recueille_clt
class Ajout_cl :
    def __init__(self, root):
        root.delete(all)
        #width=1000
        #heigth=540
        self.fen=Canvas(root, height=540, width=1000, bg="light cyan")
        self.fen.place(x=0,y=0)
        
        Label(self.fen, text="Ajouter un Client", bg="light cyan", font=("Arial 15"), fg="blue2").place(x=300, y=80)
        
        Label(self.fen, text="Identifiant :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=160)
        self.id=Entry(root, font=("Arial 12"))
        self.id.place(x=420, y=160)
        
        Label(self.fen, text="Nom :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=240)
        self.nom=Entry(self.fen, font=("Arial 12"))
        self.nom.place(x=420, y=240)
        
        Label(self.fen, text="Metier :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=320)
        self.metier=Entry(self.fen, font=("Arial 12"))
        self.metier.place(x=420, y=320)
        
        Label(self.fen, text="Demande :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=400)
        self.demande=Entry(self.fen, font=("Arial 12"))
        self.demande.place(x=420, y=400)
        
        Button(self.fen, text="    enregistrer     ", font=("Arial 12"), bg="blue2",fg="black",
               command=lambda: recueille_clt(self.fen, self.id.get(), self.nom.get(), self.metier.get(), self.demande.get())).place(x=350, y=450)