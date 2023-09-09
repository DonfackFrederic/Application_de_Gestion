from tkinter import *
from register import Register
from mot_oublie import oublie
from home import Home
from random import randint
class Login:
    def __init__(self, root, width, height):
        self.width=width
        self.height=height
        self.page=Canvas(root, width=width, height=height, bg="gray2")
        self.i=0
        while self.i<40:
               self.x=randint(0,1200)
               self.y=randint(0,600) 
               self.r=randint(20,50) 
               self.c=randint(0,4)
               self.color=["red","purple","orange", "yellow", "blue"]
               self.cercle=self.page.create_oval(self.x, self.y, self.x + self.r, self.y + self.r, fill=self.color[self.c])
               self.i+=1
        Label(self.page, text="Login", fg="blue2", bg="gray2", font=("Arial", 30)).place(x=500, y=80)
        Label(self.page, text="Username :", fg="white", bg="gray2", font=("Arial", 15)).place(x=350, y=200)
        
        #username
        self.Username=Entry(self.page, font=("Arial", 15))
        self.Username.place(x=550, y=200)
        
        #password
        Label(self.page, text="Password :", bg="gray2", fg="white", font=("Arial", 15) ).place(x=350, y=300)
        self.password=Entry(self.page, font=("Arial", 15), show="*")
        self.password.place(x=550, y=300)
        
        #boutton
        
        Button(self.page, text="    Se connecter  ", bg="blue2", font=("Arial 15"),bd=0,
               command= lambda: Home(self.page, self.width, self.height, self.Username.get(), self.password.get())
               ).place(x=490, y=400)
        
        
        # option
        Button(self.page, bg="gray2", text="mot de passe oublié ",bd=0, fg="blue2" ,font=("Arial 12"),
               command= lambda: oublie(self.page, self.width, self.height),
               ).place(x=420, y=470)
        Label(self.page, text="ou", fg="white", bg="gray2", font=("Arial 12")).place(x=590, y=470)
        Button(self.page, bg="gray2", text="s'inscrire",bd=0, fg="blue2", font=("Arial 12"),
               command= lambda: Register(self.page, self.width, self.height)).place(x=670, y=470)
        self.page.place(x=0, y=0)
        
        
        
        
        
        
       