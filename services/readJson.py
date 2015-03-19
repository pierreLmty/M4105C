#!/usr/bin/env python3.4

import json
from model.activity import Activity
from model.equipment import Equipment
from model.installation import Installation

class ReadJSON:

	def __init__(self, path):
		self.path = open(path)
		self.result = []
		
	def readActivity(self):
		data = json.load(self.path)
		
		for row in data["data"]:
			self.result.append(Activity(row["EquipementId"], row["ActLib"]))
			
	def readEquipment(self):
		data = json.load(self.path)
		
		for row in data["data"]:
			self.result.append(Equipment(row["EquipementId"], row["EquNom"], row["InsNumeroInstall"]))
			
	def readInstallation(self):
		data = json.load(self.path)
		
		for row in data["data"]:
			self.result.append(Installation(row["InsNumeroInstall"], row["geo"]["name"], str(row["InsNoVoie"]) + " " + str(row["InsLibelleVoie"]), row["InsCodePostal"], row["ComLib"], row["Latitude"], row["Longitude"]))
		
	def getResult(self):
		return self.result
