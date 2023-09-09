from tkinter import *
import sqlite3
from random import randint
class oublie:
    def __init__(self, root, width, height):
        self.page=Canvas(root, height=height, width=width, bg="gray2")
        self.page.place(x=0,y=0)
        self.i=0
        while self.i<40:
               self.x=randint(0,1200)
               self.y=randint(0,600) 
               self.r=randint(20,50) 
               self.c=randint(0,4)
               self.color=["red","purple","orange", "yellow", "blue"]
               self.cercle=self.page.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, fill=self.color[self.c])
               self.i+=1
        
        Label(self.page, text='Reconnaissance', bg="gray2", fg="blue2", font=("Arial 20")).place(x=460, y=120)
        self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
        self.conn=sqlite3.connect(self.data)
        self.cur=self.conn.cursor()
        self.cur.execute("select indice from user")
        txt=self.cur.fetchone()
        self.conn.close()
        
        #indice
        
        Label(self.page, text=txt, fg="white", bg="gray2", font=("Arial 12")).place(x=460, y=200)
        self.reponse=Entry(self.page, font=("Arial 12"))
        self.reponse.place(x=460, y=230)
        
        #def verification():
        #   code de veification et action
        
        
        
        #Bouton
        Button(self.page, text="    Retour    ", bg="blue2", bd=0,font=("Arial 15"),
               command=self.page.destroy).place(x=460, y=300)
        Button(self.page, text="    Verifier    ", bg="blue2", bd=0,font=("Arial 15"),
               command=lambda: verifier(self.page, self.reponse.get())
               ).place(x=620, y=300)
class verifier:
       def __init__(self,page,reponse):
              self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
              self.conn=sqlite3.connect(self.data)
              self.cur=self.conn.cursor()
              self.cur.execute("SELECT reponse, username, password FROM user")
              self.result=self.cur.fetchone()
              self.conn.close()
              if(self.result[0]==reponse):
                     self.msg=Canvas(page, width=350, height=80, bg="gray2")
                     self.msg.place(x=350, y=250)
                     msg="username= "+self.result[1]+"\n password= "+self.result[2]
                     Label(self.msg, text=msg, fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
                     Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                            command=self.msg.destroy).place(x=220, y=50)
              else:
                     self.msg=Canvas(page, width=350, height=80, bg="gray2")
                     self.msg.place(x=350, y=250)
                     Label(self.msg, text="Information Fausses", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
                     Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                     command=self.msg.destroy).place(x=220, y=50)

