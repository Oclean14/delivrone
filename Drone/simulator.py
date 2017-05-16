#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import dronekit
import dronekit_sitl
from dronekit import connect

print "Start simulator (SITL)"

sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

# Connexion du vehicule
print "Connecting to vehicle on: %s" % (connection_string,)
vehicle = connect(connection_string, wait_ready=True)


#	Ajout des listener des attributs
@vehicle.on_attribute('location.global_frame')
def global_frame_listener(self, name, val):
    print '%s attribute is: %s' % (name, val)


@vehicle.on_attribute('location.global_relative_frame')
def global_relative_frame_listener(self, name, val):
    print '%s attribute is: %s' % (name, val)


@vehicle.on_attribute('battery')
def battery_listener(self, name, val):
    print '%s attribute is: %s' % (name, val)


offsetLat = 0.5
offsetLon = 0.3
offsetAlt = 100
altitude = 50.0;
homeLocation = dronekit.LocationGlobal(-34.364114, 149.166022, 30)
gotoLocation = dronekit.LocationGlobal(-34.364114 + offsetLat, 149.166022 + offsetLon, 30 + offsetAlt);
gotoLocation.lat += 0.5;
vehicle.home_location = homeLocation

# Etat du vehicule
print
"Get all vehicle attribute values:"
print " DRONE VERSION: %s" % vehicle.version  # Version de l'autopilot
print " LOCATION CAPABILITIES: %s" % vehicle.capabilities
print " LOCATION GLOBAL FRAME: %s" % vehicle.location.global_frame  # position gps global. Altitude par rapport au niveau de la mer (MSL)
print " LOCATION GLOBAL RELATIVE FRAME: %s" % vehicle.location.global_relative_frame  # position par rapport à la base (à configurer comme on veut)
print " ATTITUDE: %s" % vehicle.attitude  # Pitch, Roll, Yaw
print " VELOCITY: %s" % vehicle.velocity  # Vitesse vx, vy, vz
print " GIMBAL: %s" % vehicle.gimbal
print " BATTERY: %s" % vehicle.battery  # tension de la batterie en millivolt / niveau de batterie restantes / alimentation en ampere si l'autopilot supporte
print " RANGEFINDER: %s" % vehicle.rangefinder  # Mesure du télémètre
print " EKF OK: %s" % vehicle.ekf_ok
print " LAST HEARTBEAT: %s" % vehicle.last_heartbeat  # le dernier message envoyé par le drone UPTIME
print " HOME LOCATION: %s" % vehicle.home_location  # La position de la base

"""
	UNINIT: Uninitialized system, state is unknown.
	BOOT: System is booting up.
	CALIBRATING: System is calibrating and not flight-ready.
	STANDBY: System is grounded and on standby. It can be launched any time.
	ACTIVE: System is active and might be already airborne. Motors are engaged.
	CRITICAL: System is in a non-normal flight mode. It can however still navigate.
	EMERGENCY: System is in a non-normal flight mode. It lost control over parts or over the whole airframe. It is in mayday and going down.
	POWEROFF: System just initialized its power-down sequence, will shut down now.
"""
print " SYSTEM STATUS: %s" % vehicle.system_status  # le status du système

print " HEADING: %s" % vehicle.heading  # Vers où le vehicule pointe [NORTH = 0]
print " IS ARMABLE: %s" % vehicle.is_armable
print " AIR SPEED: %s" % vehicle.airspeed  # correction par rapport au vent
print " GROUND SPEED: %s" % vehicle.groundspeed  # vitesse reelle du vehicule
print " ARMED: %s" % vehicle.armed
print " MODE: %s" % vehicle.mode

vehicle.simple_takeoff(altitude)
vehicle.simple_goto(gotoLocation, 20, 10)  # POint d'arrivée, vitesse en prenant en compte le vent, vitesse
# récupère les commandes à exécuter sur le vehicule
# cmds = vehicle.commands 
# cmds.download()
# cmds.wait_ready()

time.sleep(120000)

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")
