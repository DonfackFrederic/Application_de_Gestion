from tkinter import *
from fonctions import recueille_emp
class Ajout_emp:
    def __init__(self, root):
        root.delete(all)
        #width=1000
        #heigth=540
        self.fen=Canvas(root, height=540, width=1000, bg="light cyan")
        self.fen.place(x=0,y=0)
        
        Label(self.fen, text="Ajouter un Employé", bg="light cyan", font=("Arial 15"), fg="blue2").place(x=300, y=80)
        
        Label(self.fen, text="Identifiant :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=160)
        self.id=Entry(self.fen, font=("Arial 12"))
        self.id.place(x=420, y=160)
        
        Label(self.fen, text="Nom :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=240)
        self.nom=Entry(self.fen, font=("Arial 12"))
        self.nom.place(x=420, y=240)
        
        Label(self.fen, text="Poste :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=320)
        self.poste=Entry(self.fen, font=("Arial 12"))
        self.poste.place(x=420, y=320)
        
        Label(self.fen, text="Salaire :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=400)
        self.salaire=Entry(self.fen, font=("Arial 12"))
        self.salaire.place(x=420, y=400)
        
        Button(self.fen, text="    enregistrer     ", font=("Arial 12"), bg="blue2",fg="black",
               command=lambda: recueille_emp(self.fen, self.id.get(), self.nom.get(), self.poste.get(), self.salaire.get())).place(x=350, y=450)
        
       