import math, random
import time

class Battery:
	def __init__(self, lvl, maxCycle,consumption):
		self.id = 0 #TODO: generer un id automatic
		self.maxCycle = maxCycle
		self.lvl = lvl
		self.consumption = consumption

	def use(self):
		self.chargePercentage = chargePercentage - consumption

	def getChargePercentage(self):
		return self.chargePercentage
	def charge(self):
		a=0