import math, random
from Battery import *
from Log import Log as log
import math, random
from queue import *
import time
from ChargerThread import *
from BatteryChangerThread import *

class Station:
	TAG = "STATION"
	droneQueue = []
	reservationQueue = []
	status = "available"
	chargingBatteries = 0
	reservationQueue = []
	batteryList = []
	realAvailableBatteriesNumber = 0
	anticipatedAvailableBatteriesNumber = 0
	unusableBatteryList = []
	waitingRoom = []

	def __init__(self, id, position, chargedBatteries, storageCapacity, chargingTime, chargingSlots, changeDuration, failureFrequency):
		self.id = id
		self.position = position
		self.chargedBatteries = chargedBatteries
		self.storageCapacity = storageCapacity
		self.chargingTime = chargingTime
		self.chargingSlots = chargingSlots
		self.changeDuration = changeDuration
		self.failureFrequency = failureFrequency
		charger = Charger(self)
		charger.run()
		changer = BatteryChangerThread(self)
		changer.run()

	def putDroneInQueue(self, drone_id):
		self.droneQueue.append([0,drone_id])


	def putDroneInReservationQueue(self,drone,changementHour):
		self.reservationQueue.append([0,drone,None,changementHour])


	def getChargedBatteryNumber(self):
		return self.chargedBatteries



	def getAnticipatedBatteryNumber(self):
		i = 0
		# comptage du nombre de reservation non traitees
		for reservation in self.reservationQueue:
			if reservation[0] == 0:
				i = i + 1
		return self.chargedBatteries - i

	def getUnusableBatteryNumber(self):
		return self.unusableBatteryList.len()


	def getNextTimeBatteryReady(self):
		a=0
