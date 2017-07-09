# -*- coding: utf-8 -*-
from time import sleep
import math, random
import sqlite3
from threading import Thread
from Battery import Battery
from drone_state import DroneState
from Log import Log as l
from threading import Thread, Lock
from utils import *

#from Simulator import main
l.flags = l.LOG_ALL_ENABLE

class Drone:
	
	global django_status;
	django_status = [
		"0",
		"UNINIT",
		"BOOT",
		"CALIBRATING",
		"STANDBY",
		"ACTIVE",
		"CRITICAL",
		"EMERGENCY",
		"POWEROFF",
	]

	TAG = "DRONE"

	"""
		ctor
	"""
	def __init__(self, droneId = -1, homeLocation = (0,0), position = (0,0), altitude= 0, failureFrequency = 0, velocity = 1, battery = None):
		self.id = droneId
		self.homeLocation = homeLocation
		self.position = position
		self.state = DroneState.ON_LAND | DroneState.OFF
		self.failureFrequency = failureFrequency
		self.battery = battery
		self.altitude = altitude
		self.velocity = velocity
		self.packet = None
		self.deliveryList = []
		thread = Thread(target=self.consumeBattery, args=())
		thread.daemon = True                            # Daemonize thread
		thread.start()

#battery consumption
	def consumeBattery(self):
		while True:
			if self.state & DroneState.RUNNING:
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
					break
			sleep(1)

	def start(self):
		if self.battery != None and self.state & DroneState.OFF and self.state & DroneState.OUT_OF_ORDER == 0:
			self.state = DroneState.IDLE | DroneState.RUNNING | DroneState.ON_LAND
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
		if self.altitude <= 0:
			l.error(Drone.TAG, "The drone is already on the land")
			return -1

		if self.state & DroneState.IN_AIR and self.state & DroneState.RUNNING:
			self.state = DroneState.LANDING |  DroneState.RUNNING | DroneState.IN_AIR
			while self.altitude > 0 and self.state & DroneState.RUNNING:
				self.altitude = self.altitude - speed
				l.info(Drone.TAG, "Drone ID " + str(self.id) +  " landing altitude = " + str(self.altitude))
				sleep(1)

			if self.altitude > 0:
				l.error(Drone.TAG, "NO ENERGY CRASHING")
				return -1
			else:
				self.altitude = 0
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
			if self.altitude > altitude:
				l.error(Drone.TAG, "Impossible to take off to this altitude")
				return -1
			self.state = DroneState.TAKE_OFF |  DroneState.RUNNING | DroneState.IN_AIR
			while self.altitude < altitude and self.state & DroneState.RUNNING:
				self.altitude = self.altitude + speed
				l.info(Drone.TAG, "Drone ID " + str(self.id) +  " taking off altitude = " + str(self.altitude))
				sleep(1)

			if self.altitude < altitude:
				l.error(Drone.TAG, "NO ENERGY CRASHING")
				return -1
			else:
				self.altitude = altitude
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
		if self.state & DroneState.RUNNING and self.state & DroneState.IN_AIR:
			self.state = DroneState.FLYING | DroneState.RUNNING | DroneState.IN_AIR
			startPos = self.position
			distance = dist(self.position, destPoint)
			elapsed = 0.01
			l.debug(Drone.TAG, "Distance: " + str(distance))
			vecDir = vec2d_normalize(vec2d_sub(destPoint, self.position))
			vecDir = vec2d_multiply_scalar(vecDir, self.velocity)
			vecDir = vec2d_multiply_scalar(vecDir, elapsed)

			while(dist(startPos, self.position) < distance and self.state & DroneState.RUNNING):
				l.info(Drone.TAG, " direction vect : " + str(vecDir))
				self.position = vec2d_add(vecDir, self.position)
				l.info(Drone.TAG, " drone position : " + str(self.position))
				
			if dist(startPos, self.position) < distance:
				l.error(Drone.TAG, "NO ENERGY CRASHING")
				return -1
			else:
				self.position = destPoint
				self.state = DroneState.IN_AIR | DroneState.IDLE | DroneState.RUNNING
		else:
			l.error(Drone.TAG, "Please takeoff after go to a point")

	def removePacketFromWarehouse(self, landingSpeed, takeoffSpeed, packet):
		# land to retrieve the packe
		if self.land(landingSpeed) != 0:
			l.error(TAG, "Impossible to land to retrieve the packet")
			return -1
		self.packet = packet
		# takeoff again
		if self.takeoff(takeoffSpeed) != 0:
			return -1

	@classmethod
	def FindIdByStatus(self, status):
		status = django_status.index(status);
		status = str(status);
		conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
		cursor = conn.cursor()
		cursor.execute("""SELECT id FROM Drone WHERE status=\'""" + status + """\'""")
		packets = cursor.fetchall()
		conn.close()
		return packets

	@classmethod
	def UpdateStatusByID(self, id, status):
		status = django_status.index(status);
		status = str(status);
		conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
		# print("Opened database successfully");
		cursor = conn.cursor()
		# cursor.execute("UPDATE Delivery SET status=\'"+ status + "\' WHERE id=\'" + id + "\'");
		cursor.execute("UPDATE Drone SET status=? WHERE id=?", (status, id));
		conn.commit()
		cursor.close()

		# print("Operation done successfully");

	##
	#	Ajouter une nouvelle mission a effectuer
	def addDelivery(self,delivery):
		self.deliveryList.append(delivery)

	##
	# Suit les points fournit par un eventuelle calculateur de vol
	def followPoints(self, path):
		for point in path:
			self.goto(point)
