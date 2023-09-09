import sqlite3

data="D:/Code/python/gestion des entreprise/base de données/base.db"
conn=sqlite3.connect(data)
cur=conn.cursor()
req="CREATE TABLE user(nom TEXT, username TEXT, password TEXT, indice TEXT, reponse TEXT)"
cur.execute(req)
cur.execute("CREATE TABLE employe(id TEXT, nom TEXT, poste TEXT, salaire INTEGER)")
cur.execute("CREATE TABLE rdv(id TEXT, nom TEXT, debut TEXT, fin TEXT)")
cur.execute("CREATE TABLE finance(id TEXT, motif TEXT, cout INTEGER)")
cur.execute("CREATE TABLE client(id TEXT, nom TEXT, metier TEXT, demande TEXT)")
conn.close()