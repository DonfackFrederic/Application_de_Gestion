from tkinter import *
import sqlite3
from random import randint
class Register:
    def __init__(self, root, width, height):
        self.page=Canvas(root, bg="gray2", width=width, height=height)
        self.i=0
        self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
        self.conn=sqlite3.connect(self.data)
        self.cur=self.conn.cursor()
        self.cur.execute("SELECT * FROM user")
        self.result=self.cur.fetchall()
        if(self.result is None):
              while self.i<40:
                     self.x=randint(0,1200)
                     self.y=randint(0,600) 
                     self.r=randint(20,50) 
                     self.c=randint(0,4)
                     self.color=["red","purple","orange", "yellow", "blue"]
                     self.cercle=self.page.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, fill=self.color[self.c])
                     self.i+=1 
              
              Label(self.page, text="Sign Up", font=("Arial 20 "), fg="blue2", bg="gray2").place(x=580, y=80)
              #nom
              #self.cur.execute("DELETE FROM user where username=f")
              Label(self.page, text="Nom :", font=("Arial 12 "), fg="white", bg="gray2").place(x=470, y=150)
              self.Nom_r=Entry(self.page, font=("Arial 12"))
              self.Nom_r.place(x=590, y=150)
              #prenom
              Label(self.page, text="Username :", font=("Arial 12 "), fg="white", bg="gray2").place(x=470, y=200)
              self.username_r=Entry(self.page, font=("Arial 12"))
              self.username_r.place(x=590, y=200)
              #mot de passe 
              Label(self.page, text="Mot de passe :", font=("Arial 12 "), fg="white", bg="gray2").place(x=470, y=250)
              self.password_r=Entry(self.page, font=("Arial 12"), show="*")
              self.password_r.place(x=590, y=250)
              
              #option de reconnaissance et enregisterer
              
              Label(self.page, text="Reconnaissance", font=("Arial 20 "), fg="blue2", bg="gray2").place(x=530, y=290)
              op_can=Canvas(self.page, height=80, width=300, bg="gray2", highlightbackground="blue2")
              
              Label(op_can, text="indice :", bg="gray2", fg="white", font=("Arial 12 ")).place(x=10, y=15)
              op_can.place(x=470, y=350)
              self.indice=Entry(op_can, font=("Arial 12"))
              self.indice.place(x=100, y=15)
              Label(op_can, text="reponse :", bg="gray2", fg="white", font=("Arial 12 ")).place(x=10, y=55)
              self.reponse=Entry(op_can, font=("Arial 12"))
              self.reponse.place(x=100, y=55)
              
              
              Button(self.page, text="   Enregister   ", bg="blue2", bd=0, font=("Arial 15"),
                     command=lambda: enregistrer(self.page,self.Nom_r.get(), self.username_r.get(),
                                                 self.password_r.get(), self.indice.get(), self.reponse.get())
                     ).place(x=490, y=450)
              #Button(self.page, text="   reinitialiser  ",bg="blue2", bd=0, font=("Arial 15"),
                     #command=).place(x=640,y=450)
              #retour
              
              Button(self.page, text="Se connecter", fg="blue2", bg="gray2", bd=0,font=("Arial 10 "),
                     command=self.page.destroy).place(x=480, y=500)
              
              self.page.place(x=0, y=0)
        else:
               self.msg=Canvas(root, width=350, height=80, bg="gray2")
               self.msg.place(x=350, y=250)
               Label(self.msg, text="un utlisateur existe deja", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
               Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                     command=self.msg.destroy).place(x=220, y=50)

class enregistrer:
       def __init__(self,root,nom, username, password, indice, reponse):
              #sql ici
        
              if(id !="" and nom!="" and username !="" and password !="" and indice!="" and reponse!=""):
                     self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
                     self.conn=sqlite3.connect(self.data)
                     self.cur=self.conn.cursor()
                     #self.req="CREATE TABLE user(nom TEXT, username TEXT, password TEXT, indice TEXT, reponse TEXT)"
                     self.req="INSERT INTO user(nom, username, password, indice, reponse) VALUES(?,?,?,?,?)"
                     self.val=(nom, username, password, indice, reponse)
                     self.cur.execute(self.req, self.val)
                     self.conn.commit()
                     self.conn.close()
                     self.msg=Canvas(root, width=350, height=80, bg="gray2")
                     self.msg.place(x=350, y=250)
                     Label(self.msg, text="Informations enregistrés", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
                     Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                            command=self.msg.destroy).place(x=200, y=50)
              else:
                     self.msg=Canvas(root, width=350, height=80, bg="gray2")
                     self.msg.place(x=350, y=250)
                     Label(self.msg, text="certain(s) champs est (sont) vide(s)", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
                     Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                     command=self.msg.destroy).place(x=220, y=50)
