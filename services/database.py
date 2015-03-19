#!/usr/bin/env python3.4

import sqlite3

class Database:


	def __init__(self, path):
		self.conn = sqlite3.connect(path)
		self.path = path
		
		
	def create_DB(self):
	
		c = self.conn.cursor()

		c.execute("DROP TABLE IF EXISTS installation")
		c.execute("CREATE TABLE installation (number INTEGER PRIMARY KEY, name VARCHAR, address VARCHAR, zipCode INTEGER, city VARCHAR, latitude DECIMAL, longitude DECIMAL)")

		c.execute("DROP TABLE IF EXISTS equipement")
		c.execute("CREATE TABLE equipement (number INTEGER PRIMARY KEY, name VARCHAR, installationNumber INTEGER, FOREIGN KEY(installationNumber) REFERENCES installation(number))")

		c.execute("DROP TABLE IF EXISTS activite")
		c.execute("CREATE TABLE activite (number INTEGER PRIMARY KEY, name VARCHAR)")
	
		c.execute("DROP TABLE IF EXISTS ep_ac_temp")
		c.execute("CREATE TABLE ep_ac_temp (equip_num_temp INTEGER, act_num_temp INTEGER, act_name_temp VARCHAR)")

		c.execute("DROP TABLE IF EXISTS equipement_activite")
		c.execute("CREATE TABLE equipement_activite (number_equipment INTEGER, number_activity INTEGER, FOREIGN KEY(number_equipment) REFERENCES equipement(number), FOREIGN KEY(number_activity) REFERENCES activite(number))")

		self.commit_DB()

	def Insert_In_Installation(self, installation):
		c = self.conn.cursor()
		c.execute('INSERT INTO installation(number, name, address, zipCode, city, latitude, longitude) VALUES(:number, :name, :address, :zipCode, :city, :latitude, :longitude)',
                          {'number':installation.number, 'name':installation.name, 'address':installation.address, 'zipCode':installation.zipCode, 'city':installation.city, 'latitude':installation.latitude, 'longitude':installation.longitude})


	def Insert_In_Equipment(self, equipement):
		c = self.conn.cursor()
		c.execute('INSERT INTO equipement(number, name, installationNumber) VALUES(:number, :name, :installationNumber)',
                          {'number':equipement.number, 'name':equipement.name, 'installationNumber':equipement.installationNumber})


	def Insert_In_eq_ac_temp(self, eq_ac_temp):
		c = self.conn.cursor()
		c.execute('INSERT INTO ep_ac_temp(equipmentNumber, activityNumber, activityName) VALUES (:equipmentNumber, :activityNumber, :activityName)',
                          {'equipmentNumber':eq_ac_temp.equip_num_temp, 'act_num_temp':eq_ac_temp.act_num_temp, 'activityName':act_name_temp})

		
	def Insert_In_Activity(self, activite):
		c = self.conn.cursor()
		c.execute('INSERT INTO activite(number, name) VALUES(:number, :name)',
                          {'number':activite.number, 'name':activite.name})

	
	def commit_DB(self):
		self.conn.commit()
	
	
	def disconnect(self):
		self.conn.close()
