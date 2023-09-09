from tkinter import *
from login import Login
#page accueille

class app:
    def __init__(self):
        self.root=Tk()
        self.root.title("Gestion du personel")
        self.root.geometry("1200x600+75+60")
        self.root.resizable(width=False, height=False)
        Login(self.root, width=1200, height=600)
        self.root.mainloop()

ma_fen=app()
