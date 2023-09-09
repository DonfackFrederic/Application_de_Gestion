from tkinter import *
import sqlite3
class statistique:
    def __init__(self, root, width, height):
        root.delete(all)
        #partie bouton
        
        self.bouton=Canvas(root, width=width, height=60, bg="gray8")
        self.bouton.place(x=0,y=0)
        
        self.corp=Canvas(root, width=width, height=height-60, bg="light cyan")
        self.corp.place(x=0, y=60)
        
        self.data="D:/Code/python/gestion des entreprise/base de données/base.db"
        self.conn=sqlite3.connect(self.data)
        self.cur=self.conn.cursor()
        #employe
        self.cur.execute("SELECT COUNT(id) FROM employe")
        resut1=self.cur.fetchall()
        nb_emp=resut1[0]
        #client
        self.cur.execute("SELECT COUNT(id) FROM client")
        resut2=self.cur.fetchall()
        nb_clt=resut2[0]
        #rdv
        self.cur.execute("SELECT COUNT(id) FROM rdv")
        resut3=self.cur.fetchall()
        nb_rdv=resut3[0]
        
        #nombre de facture
        self.cur.execute("SELECT COUNT(id) FROM finance")
        resut4=self.cur.fetchall()
        nb_fac=resut4[0]
        
        #somme des depenses
        self.cur.execute("SELECT SUM(cout) FROM finance")
        resut5=self.cur.fetchall()
        cout=resut5[0]
        
        Label(root, font=("Arial 15"), bg="light cyan" ,text="nombre d'employés :").place(x="300", y=100)
        Label(root, font=("Arial 15"), bg="light cyan" ,text=nb_emp).place(x=600, y=100)
        Label(root, font=("Arial 15"), bg="light cyan" ,text="nombre de rendez vous :").place(x="300", y=150)
        Label(root, font=("Arial 15"), bg="light cyan" ,text=nb_rdv).place(x=600, y=150)
        Label(root, font=("Arial 15"), bg="light cyan" ,text="nombre de factures :").place(x="300", y=200)
        Label(root, font=("Arial 15"), bg="light cyan" ,text=nb_fac).place(x=600, y=200)
        Label(root, font=("Arial 15"), bg="light cyan" ,text="nombre de clients :").place(x="300", y=250)
        Label(root, font=("Arial 15"), bg="light cyan" ,text=nb_clt).place(x=600, y=250)
        Label(root, font=("Arial 15"), bg="light cyan" ,text="Depenses Totales :").place(x="300", y=300)
        Label(root, font=("Arial 15"), bg="light cyan" ,text=cout).place(x=600, y=300)
        