# -*- coding: utf-8 -*-
import math, random
import time
from threading import Thread
from Battery import Battery
#from Simulator import main

class Drone(Thread) :
	
	drone_status = {
		0 : "free in warehouse",
		1 : "flying, executing mission",
		2 : "Taking packet in warehouse",
		3 : "Waiting for battery changement",
		4 : "Changing battery",
		5 : "Free flying",
		6 : "In maintenance",
		7 : "Delivering"
	}
	
	"""
		ctor
	
	def __init__(self, homeLocation, position, failureFrequency, averageSpeed, battery):
		Thread.__init__(self)
		self.homeLocation = homeLocation 
		self.position = position
		self.status = "free"
		self.failureFrequency = failureFrequency
		self.averageSpeed = averageSpeed
		self.battery = battery
	"""
	__id = 0
	def __init__(self, position, averageSpeed):
		Thread.__init__(self)
		Drone.__id += 1
		self.id = Drone.__id
		self.position = position
		self.status = 1
		self.startingPosition = position
		self.averageSpeed = averageSpeed
		self.battery = Battery(300, 100, 2)
		
	#	Toute la logique du drone
	#	- Perte de batterie
	#	- Deplacement
	def run(self):
		while not(self.isOnTopOfDirection()) and self.status == 1:
			print("I'm at", self.position, " and I'm going to ", self.direction, " i have battery level of ", self.battery.chargePercentage)
			distance = math.sqrt(self.square(self.direction[0] - self.startingPosition[0]) + self.square(self.direction[1] - self.startingPosition[1]))
			speedVector = [(self.averageSpeed * (self.direction[0] - self.startingPosition[0])/distance), (self.averageSpeed * (self.direction[1] - self.startingPosition[1])/distance)]
			self.position[0] = self.position[0] + speedVector[0]
			self.position[1] = self.position[1] + speedVector[1]
			self.battery.use();
			if self.battery.chargePercentage <= 0:
				self.status = "noenergy"
			time.sleep(0.1)
		

	# TODO: ajouter le commentaire de la fonction setDirection
	def setDirection(self, direction):	
		self.direction = direction

	##
	#	Ajouter une nouvelle mission a effectuer
	def addDelivery(self,delivery):
		self.deliveryList.append(delivery)

	#TODO: ajouter le commentaire de la fonction executeDelivery
	def executeDelivery(self, delivery):
		for pos in delivery:
			i = 1
		
	##
	#	Recupere le niveau de charge du drone
	def getChargeLevel(self):
		return self.battery.lvl

	##
	#	Recupere l'etat du drone
	def getStatus(self):
		return self.status

	##
	#	Renseigne l'etat du drone
	def setStatus(self, status):
		self.status = status
	##	
	# Recupere la direction du drone
	def getDirection(self):
		return self.direction
	##	
	# Suit les points fournit par un eventuelle calculateur de vol
	def followPoints(self):
		return

	def square(self,x):
		return x*x

	# TODO: ajouter le commentaire de la fonction
	def isOnTopOfDirection(self):
		distance = math.sqrt(self.square(self.direction[0] - self.position[0]) + self.square(self.direction[1] - self.position[1]))
		print(distance)
		if(distance > 3):
			return False
		else:
			return True

	def subscribeToStation(self, station):
		self.status = 4
		station.droneQueue.append(self)
