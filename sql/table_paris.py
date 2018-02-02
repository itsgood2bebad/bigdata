#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3

class Mabase():
	def __init__(self):
		self.conn = sqlite3.connect('mabase.db')

	def creer(self):
		c = self.conn.cursor()

		try:
			c.execute('create table vente (id INTEGER PRIMARY KEY,bookname VARCHAR(50), sales INTEGER)')

			c.execute('insert into vente values (null,"bookA","2")')
			c.execute('insert into vente values (null,"bookB","8")')
			c.execute('insert into vente values (null,"bookC","1")')
			c.execute('insert into vente values (null,"bookB","6")')

			self.conn.commit()

			c.close()
			print("ok table")
			return True

		except:
			self.close()
			return False
	
	def lire(self):

		c = self.conn.cursor()
		c.execute("SELECT * FROM vente")
		for row in c:
			print (row)
		c.close()

mabase = Mabase()
if not mabase.creer():
	mabase.lire()
