#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import sqlite3
 
class Mabase():
 
	def __init__(self):
 
		self.conn = sqlite3.connect('mabase.db')
 
	def creer(self):
		"""	Créer une simple base.
			Renvoi True si reussie, False si déjà créée. """
 
		# Obtention d'un curseur
		c = self.conn.cursor()
 
		# Créer une table
		try:
			c.execute('create table comptes (id INTEGER PRIMARY KEY,signature VARCHAR(50), compteur INTEGER)')
			# Inserer deux lignes de données
			c.execute('insert into comptes values (null,"bookA","2")')
			c.execute('insert into comptes values (null,"bookB","4")')
 
			# Sauvegarder les modifications
			self.conn.commit()
 
			# Fermer le curseur
			c.close()
			print "Création de la base réussie."
			return True
 
		except:
			# Fermer le curseur
			c.close()
			return False
 
	def lire(self):
		"""	"""
		c = self.conn.cursor()
		c.execute("SELECT * FROM comptes")
		for row in c:
			print row
		c.close()
 
# Création de l'instance de classe
mabase = Mabase()
if not mabase.creer():	# Si la méthode creer() renvoi False, lire la base
	mabase.lire()