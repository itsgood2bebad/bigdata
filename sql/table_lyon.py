import sqlite3
#creation base de donnés en python
class Mabase():
	def __init__(self): #creation d'un objet
		self.conn = sqlite3.connect('mabase.db')
#création d'une simple base 
	def creer(self):
		c = self.conn.cursor()
#creation de la base avec les valeurs comme sur l'exercice
		try:
			c.execute('create table vente (id INTEGER PRIMARY KEY,bookname VARCHAR(50), sales INTEGER)')

			c.execute('insert into vente values (null,"bookB","15")')
			c.execute('insert into vente values (null,"bookA","2")')
			c.execute('insert into vente values (null,"bookC","7")')
			c.execute('insert into vente values (null,"bookA","1")')
# sauvegarde des modifications
			self.conn.commit()

			c.close()
			print("ok table")
			return True

		except:
			self.close()
			return False
	#affichage du tableau
	def lire(self):

		c = self.conn.cursor()
		c.execute("SELECT * FROM vente")
		for row in c:
			print (row)
		c.close()
#appel des fonctions 
mabase = Mabase()
if not mabase.creer():
	mabase.lire()