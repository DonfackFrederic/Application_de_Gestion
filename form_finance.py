from tkinter import *
from fonctions import recueille_finc
class facture:
    def __init__(self, root):
        root.delete(all)
        #width=1000
        #heigth=540
        
        self.fen=Canvas(root, height=540, width=1000, bg="light cyan")
        self.fen.place(x=0,y=0)
        Label(self.fen, text="Ajouter une Depense", bg="light cyan", font=("Arial 15"), fg="blue2").place(x=300, y=80)
        
        Label(self.fen, text="Identifiant :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=160)
        self.id=Entry(self.fen, font=("Arial 12"))
        self.id.place(x=420, y=160)
        
        Label(self.fen, text="Motif :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=240)
        self.motif=Entry(self.fen, font=("Arial 12"))
        self.motif.place(x=420, y=240)
        
        Label(self.fen, text="Cout :", bg="light cyan", font=("Arial 12"), fg="black").place(x=300, y=320)
        self.cout=Entry(self.fen, font=("Arial 12"))
        self.cout.place(x=420, y=320)
        
        Button(self.fen, text="    enregistrer     ", font=("Arial 12"), bg="blue2",fg="black",
               command=lambda: recueille_finc(self.fen, self.id.get(), self.motif.get(), self.cout.get())).place(x=350, y=450)