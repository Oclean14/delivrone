import math, random
import time

class Battery:
	__id = 0
	def __init__(self, maxCycle, chargePercentage, consumption):
		Battery.__id += 1
		self.id = Battery.__id
		self.maxCycle = maxCycle
		self.chargePercentage = chargePercentage
		self.consumption = consumption
		
	def use(self):
		self.chargePercentage = self.chargePercentage - self.consumption

	def getChargePercentage(self):
		return self.chargePercentage
		
	def charge(self):
		a=0