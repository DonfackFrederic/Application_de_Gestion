from tkinter import *
import sqlite3

class recueille_emp:
    def __init__(self, root, id, nom, poste, salaire):
        self.msg=Canvas(root, width=350, height=80, bg="gray2")
        self.msg.place(x=350, y=250)
        #sql ici
        
        
        if(id !="" and nom!="" and poste !="" and salaire !=""):
            self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
            self.conn=sqlite3.connect(self.data)
            self.cur=self.conn.cursor()
            #self.cur.execute("CREATE TABLE employe(id TEXT, nom TEXT, poste TEXT, salaire INTEGER)")
            self.cur.execute("INSERT INTO employe(id, nom, poste, salaire) VALUES(?,?,?,?)",(id, nom, poste, salaire))
            self.conn.commit()
            self.conn.close()
            Label(self.msg, text="Informations enregistrés", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
            Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=200, y=50)
        else:
            Label(self.msg, text="certain(s) champs est (sont) vide(s)", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
            Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=220, y=50)


class recueille_rdv:
     def __init__(self, root, id, nom, debut, fin):
        self.msg=Canvas(root, width=350, height=80, bg="gray2")
        self.msg.place(x=350, y=250)
        #sql ici
        
        if(id !="" and nom!="" and debut !="" and fin !=""):
            self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
            self.conn=sqlite3.connect(self.data)
            self.cur=self.conn.cursor()
            #self.cur.execute("CREATE TABLE rdv(id TEXT, nom TEXT, debut TEXT, fin TEXT)")
            self.cur.execute("INSERT INTO rdv(id, nom, debut, fin) VALUES(?,?,?,?)",(id, nom, debut, fin))
            self.conn.commit()
            self.conn.close()
            Label(self.msg, text="Informations enregistrés", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
            Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=200, y=50)
        else:
            Label(self.msg, text="certain(s) champs est (sont) vide(s)", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
            Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=220, y=50)

class recueille_finc:
     def __init__(self, root, id, motif, cout):
        self.msg=Canvas(root, width=350, height=80, bg="gray2")
        self.msg.place(x=350, y=250)
        #sql ici
        
        if(id !="" and motif !="" and cout !=""):
            self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
            self.conn=sqlite3.connect(self.data)
            self.cur=self.conn.cursor()
            #self.cur.execute("CREATE TABLE finance(id TEXT, motif TEXT, cout INTEGER)")
            self.cur.execute("INSERT INTO finance(id, motif, cout) VALUES(?,?,?)",(id, motif, cout))
            self.conn.commit()
            self.conn.close()
            Label(self.msg, text="Informations enregistrés", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
            Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=200, y=50)
        else:
            Label(self.msg, text="certain(s) champs est (sont) vide(s)", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
            Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=220, y=50)

class recueille_clt:
     def __init__(self, root, id, nom, metier, demande):
        self.msg=Canvas(root, width=350, height=80, bg="gray2")
        self.msg.place(x=350, y=250)
        #sql ici
        
        if(id !="" and nom!="" and metier !="" and demande !=""):
            self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
            self.conn=sqlite3.connect(self.data)
            self.cur=self.conn.cursor()
            #self.cur.execute("CREATE TABLE client(id TEXT, nom TEXT, metier TEXT, demande TEXT)")
            self.cur.execute("INSERT INTO client(id, nom, metier, demande) VALUES(?,?,?,?)",(id, nom, metier, demande))
            self.conn.commit()
            self.conn.close()
            Label(self.msg, text="Informations enregistrés", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
            Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=200, y=50)
        else:
            Label(self.msg, text="certain(s) champs est (sont) vide(s)", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
            Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=220, y=50)

class supprimer:
    def __init__(self, root, table, id):
        self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
        self.conn=sqlite3.connect(self.data)
        self.cur=self.conn.cursor()
        self.req="DELETE FROM "+table+" WHERE id=?"
        self.cur.execute(self.req,(id,))
        self.conn.commit()
        self.conn.close()
        self.msg=Canvas(root, bg="gray2", width=350, height=80)
        Label(self.msg, text="Informations supprimées veuillez actualiser", fg="white", bg="gray2", font="Arial 12").place(x=10, y=5)
        Button(self.msg, text="         Ok         ", bg="blue2", font=("Arial 12"), fg="White",
                command=self.msg.destroy).place(x=220, y=50)
        self.msg.place(x=350, y=250)