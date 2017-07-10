import math, random
import time

class Battery:
	__id = 0
	def __init__(self, maxCycle, chargePercentage, consumption):
		Battery.__id += 1
		self.id = Battery.__id
		self.cycleDone = 0
		self.chargePercentage = chargePercentage
		self.consumption = consumption
		self.chargeLevel = 100

	def use(self):
		self.chargePercentage = self.chargePercentage - self.consumption

	def getChargePercentage(self):
		return self.chargePercentage

	def charge(self, delta):
		self.chargeLevel += delta

	def isUsable(self):
		if self.cycleDone >= maxCycle:
			return False
		else:
			return True
