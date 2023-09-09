from tkinter import *
import sqlite3
from employé import employe
from client import client
from rendez_vous import rendez_vous
from Finance import finance
from statistque import statistique
class Home:
    def __init__(self,root, width, height, username, password):
        # ici on placera un if qui pour verifer le mot de passe  il englobera le code d'interface
        self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
        self.conn=sqlite3.connect(self.data)
        self.cur=self.conn.cursor()
        self.cur.execute("SELECT password FROM user WHERE username=?",(username,))
        self.result=self.cur.fetchone()
        self.conn.close()
        if(self.result is not None and self.result[0]==password):
        
              # corp
              self.page=Canvas(root, width=width, height=height, bg="gray2")
              self.page.place(x=0,y=0)
              
              
              #menu Gauche
              self.gauche=Canvas(self.page, height=height-61, width=200, bg="gray8")
              self.gauche.place(x=0,y=60)
              
              #label de possession
              self.user=Canvas(self.page, height=60, width=200, bg="blue2")
              self.user.place(x=0,y=0)
              Label(self.user, text="  bienvenu User", fg='white', bg="blue2", font=("Arial 12")).place(x=10, y=10)
              Label(self.user, text=username, fg='gold', bg="blue2", font=("Arial 15")).place(x=5, y=30)
              
              #bouton retour
              Button(self.gauche, text="  Se deconnecter   ", bg="blue2", font=("Arial 15"), fg="white",
                     command=self.page.destroy).place(x=10, y=490)
              
              
              #Tableau d'affichage
              self.width=1000
              self.heigth=height
              self.droite=Canvas(self.page, width=self.width, height=self.heigth, bg="gray14")
              self.droite.place(x=201, y=0)
              
              #menu
              #ici je ferai les option avec des boutons
              
              #employer
              Button(self.gauche, text="        Employés      ", bg="blue2", font=("Arial 15"), fg="white",
                     command=lambda: employe(self.droite, self.width, self.heigth),
                     ).place(x=10, y=50)
              #Rendez-vous
              Button(self.gauche, text="    Rendez-vous     ", bg="blue2", font=("Arial 15"), fg="white",
                     command= lambda: rendez_vous(self.droite, self.width, self.heigth)
                     ).place(x=10, y=100)
              #Finance
              Button(self.gauche, text="       Finances        ", bg="blue2", font=("Arial 15"), fg="white",
                     command= lambda: finance(self.droite, self.width, self.heigth)
                     ).place(x=10, y=150)
              #Clients
              Button(self.gauche, text="        Clients          ", bg="blue2", font=("Arial 15"), fg="white",
                     command= lambda : client(self.droite, self.width, self.heigth)
                     ).place(x=10, y=200)
              #statistique
              Button(self.gauche, text="     Statistiques      ", bg="blue2", font=("Arial 15"), fg="white",
                     command= lambda: statistique(self.droite, self.width, self.heigth)
                     ).place(x=10, y=250)
        else:
              self.msg=Canvas(root, width=350, height=80, bg="gray2")
              self.msg.place(x=350, y=250)
              Label(self.msg, text="verifier le username ou le mot de passe", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
              Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                     command=self.msg.destroy).place(x=220, y=50)

              