import math, random
import time
from Battery import *
from Log import Log as log

class Station:
	TAG = "STATION"
	def __init__(self, name, position, chargingBatteries, chargedBatteries, storageCapacity, chargingTime, chargingSlots, changeDuration, failureFrequency):
		self.name = name
		self.position = position
		self.chargingBatteries = chargingBatteries
		self.chargedBatteries = chargedBatteries
		self.storageCapacity = storageCapacity
		self.chargingTime = chargingTime
		self.chargingSlots = chargingSlots
		self.changeDuration = changeDuration
		self.failureFrequency = failureFrequency

	def chargeNewBattery(self, battery):
		log.info(TAG, "Station "+ self.name + " Ajout d'une nouvelle batterie en charge")  
	def addBatteryToChargedStorage(self, battery):
		log.info(TAG, "Station " + self.name + " Ajout d'une nouvelle batterie disponible")

	def createStock(self):
		for i in range(0,numberBattery):
			batteryList.append(Battery())




