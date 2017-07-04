# -*- coding: utf-8 -*-
from time import sleep
from threading import Thread
from Battery import Battery
from drone_state import DroneState
from Log import Log as l
from threading import Thread
#from Simulator import main
l.flags = l.LOG_ALL_ENABLE

class Drone:

	TAG = "DRONE"

	"""
		ctor
	"""
	def __init__(self, droneId = -1, homeLocation = (0,0), position = (0,0,0), failureFrequency = 0, velocity = (0,0), battery = None):
		self.id = droneId
		self.homeLocation = homeLocation
		self.position = position
		self.state = DroneState.ON_LAND | DroneState.OFF
		self.failureFrequency = failureFrequency
		self.battery = battery
		self.velocity = velocity
		self.packet = None
		self.deliveryList = []

	def consumeBattery(self):
		while self.state & DroneState.RUNNING:
				l.info(Drone.TAG, "Battery consumption lvl: " + str(self.battery.chargePercentage))
				self.battery.use()
				# percentage 0 attery
				if self.battery.chargePercentage <= 0:
					if self.state & DroneState.IN_AIR:
						l.error(Drone.TAG, "WARNING CRASH !!!")
						self.state = DroneState.OUT_OF_ORDER | DroneState.ON_LAND
					else:
						l.info(Drone.TAG, "WARNING NO BATTERY")
						self.state = DroneState.ON_LAND | DroneState.OFF
				sleep(1)

	def start(self):
		if self.battery != None and self.state & DroneState.OFF and self.state & DroneState.OUT_OF_ORDER == 0:
			self.state = DroneState.IDLE | DroneState.RUNNING | DroneState.ON_LAND
			consumeBatteryTh = Thread(target = self.consumeBattery)
			consumeBatteryTh.setDaemon(True)
			consumeBatteryTh.start()
			return 0
		elif self.battery != None and self.state & DroneState.OUT_OF_ORDER == 0:
			l.info(Drone.TAG, "The drone is already started")
		elif self.battery != None and self.state & DroneState.OFF:
			l.info(Drone.TAG, "Drone out of service please repair it")
		else:
			l.info(Drone.TAG, "Can't start drone please plug a battery")

		return -1

	def stop(self):
		if self.battery != None and self.state & DroneState.RUNNING:
			if self.state & DroneState.IN_AIR:
				l.debug(Drone.TAG, "Stopping drone in air. Bad idea. CRASHING !")
				self.state = DroneState.OUT_OF_ORDER | DroneState.ON_LAND | DroneState.OFF
			else:
				l.debug(Drone.TAG, "Shut off the drone")
				self.state = DroneState.OFF | DroneState.ON_LAND
			return 0
		elif self.battery != None:
			l.info(Drone.TAG, "Can't stop drone not started")
			return -1
		else:
			l.info(Drone.TAG, "Irrelevant to stop drone. No battery found plugged into the drones")
			return -1


	def land(self, speed):
		if self.state & DroneState.IN_AIR and self.state & DroneState.RUNNING:
			self.state = DroneState.LANDING |  DroneState.RUNNING | DroneState.IN_AIR
			while self.position[2] > 0:
				self.position = (self.position[0], self.position[1], self.position[2] - speed)
				l.info(Drone.TAG, "Drone ID " + str(self.id) +  " landing altitude = " + str(self.position[2]))
				sleep(1)
			self.position = (self.position[0], self.position[1], 0)
			self.state = DroneState.ON_LAND | DroneState.RUNNING | DroneState.IDLE
			return 0
		elif self.state & DroneState.RUNNING:
			l.error(Drone.TAG, "The drone is not in the air impossile to land")
			return -1
		else:
			l.error(Drone.TAG, "The drone is not running. Please call start() method before")
			return -1


	def takeoff(self, altitude, speed):
		if self.state & DroneState.ON_LAND and self.state & DroneState.RUNNING:
			self.state = DroneState.TAKE_OFF |  DroneState.RUNNING
			while self.position[2] < altitude:
				self.position = (self.position[0], self.position[1], self.position[2] + speed)
				l.info(Drone.TAG, "Drone ID " + str(self.id) +  " taking off altitude = " + str(self.position[2]))
				sleep(1)
			self.position = (self.position[0], self.position[1], altitude)
			self.state = DroneState.IN_AIR | DroneState.IDLE | DroneState.RUNNING
			return 0
		elif self.state & DroneState.RUNNING:
			l.error(Drone.TAG, "The drone is not on the land impossile to takeoff")
			return -1
		else:
			l.error(Drone.TAG, "The drone is not running. Please call start() method before")
			return -1

	#TODO: implement the goto method
	def goto(self, destPoint):
		return

	def removePacketFromWarehouse(self, landingSpeed, takeoffSpeed, packet):
		# land to retrieve the packe
		if self.land(landingSpeed) != 0:
			l.error(TAG, "Impossible to land to retrieve the packet")
			return -1
		self.packet = packet
		# takeoff again
		if self.takeoff(takeoffSpeed) != 0:
			return -1

	##
	#	Ajouter une nouvelle mission a effectuer
	def addDelivery(self,delivery):
		self.deliveryList.append(delivery)

	##
	# Suit les points fournit par un eventuelle calculateur de vol
	def followPoints(self, path):
		for point in path:
			self.goto(point)
