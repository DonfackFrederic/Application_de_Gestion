from tkinter import *
from tkinter import ttk
import sqlite3
from fonctions import supprimer
class list_rdv:
    def __init__(self,root):
        root.delete(all)
        #width=1000
        #heigth=540
        self.fen=Canvas(root, height=540, width=1000, bg="light cyan")
        self.fen.place(x=0,y=0)
        #creation du tableau
        self.tab=ttk.Treeview(self.fen, columns=(1,2,3,4), height=5, show="headings")
        Label(self.fen, text="liste des rendez-vous", fg="blue2", bg="light cyan", font=("Arial 15")).place(x=400, y=100)
        #headings
        self.tab.heading(1,text="ID")
        self.tab.heading(2,text="Motif")
        self.tab.heading(3,text="heure de debut")
        self.tab.heading(4,text="heure de fin")
        
        self.tab.column(1, width=50)
        self.tab.column(2, width=200)
        self.tab.column(3, width=200)
        self.tab.column(4, width=200)
        self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
        self.conn=sqlite3.connect(self.data)
        self.cur=self.conn.cursor()
        self.cur.execute("SELECT id, nom, debut, fin  FROM rdv")
        self.result=self.cur.fetchall()
        self.conn.close()
        for rdv in self.result:
            self.tab.insert("",END, values=rdv)
        #place
        #suppression
        self.supp=Canvas(self.fen, bg="deep sky blue", height=100, width=480)
        Label(self.supp, text="suppression dans la liste", font=('Arial 15'), bg="deep sky blue").place(x=100, y=7)
        Label(self.supp, text="id de l'element à supprimer", bg="deep sky blue").place(x=10, y=40)
        self.elm=Entry(self.supp, width=40)
        self.elm.place(x=200, y=40)
        table="rdv"
        Button(self.supp, text="          supprimer          ", bg="blue2",
               command=lambda: supprimer(self.fen, table, self.elm.get())).place(x=200, y=70)
        self.supp.place(x=250,y=330)
        self.tab.place(x=250, y=150)