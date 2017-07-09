"""Ce fichier permet de renseigner tous les parametres"""
from Drone import Drone
from Battery import Battery
from Log import Log
#Aerianspace

aerianSpace = []

#Drone

numberDrone = 100
averageSpeed = 10
failureFrequency = 0.1 #panne/heure de vol/drone

#Station

numberStation = 10
batteriesPerStation = 20
chargingTime = 3 #(pourcentage de accumule par minute)
changingTime = 60 #(nombre de seconde pour le changement de batterie)

#Delivery

mode = 1 # 0 : utilisation des missions du site uniquement, 1 : mode auto, 2 : mode hybride
deliveryFrequency = 2 #frequence de creation de mission par minute


#Batterie

consumption = 3 # consommation en pourcentage de batterie par minute en vol pour simplifier
maxCycle = 300 # nombre de cycle de rechargement des batteries

#Time
startAt = "100416052000"
oneSecond = 0.0001

#Stock in Warehouse
motorsNumber = 60
motorPrice = 100 #euro
propellersNumber = 100
propellerPrice = 30

stationList = []
droneList = []
WarehouseList = []

"""Ce fichier permet de renseigner tous les parametres"""

# Aerianspace

# aerianSpace = []

# Drone

# numberDrone = 100
# averageSpeed = 30
# failureFrequency = 0.1 #panne/heure de vol/drone

# Station

# numberStation = 10
# batteriesPerStation = 20
# chargingTime = 3 #(pourcentage de accumule par minute)
# changingTime = 60 #(nombre de seconde pour le changement de batterie)

# Delivery

# mode = 1 # 0 : utilisation des missions du site uniquement, 1 : mode auto, 2 : mode hybride
# deliveryFrequency = 2 #frequence de creation de mission par minute


# Batterie

# consumption = 3 # consommation en pourcentage de batterie par minute en vol pour simplifier
# maxCycle = 300 # nombre de cycle de rechargement des batteries

# Time
# startAt = "100416052000"
# oneSecond = 0.0001

# Stock in Warehouse
# motorsNumber = 60
# motorPrice = 100 #euro
# propellersNumber = 100
# propellerPrice = 30

# stationList = []
# droneList = []
# WarehouseList = []

import json
from pprint import pprint
from Log import Log as log
from WorldState import WorldState
from Drone import Drone
from Battery import Battery
from Station import Station
from Renderer import Renderer
from Scheduler import Scheduler
TAG = "MAIN"
log.flags = log.LOG_ALL_ENABLE
# log test

log.info(TAG, "Simulator started");

with open("config.json") as simu_cfg_file:
    simu_cfg = json.load(simu_cfg_file)

# affiche le json charge
# pprint(simu_cfg);

# Ajout des objets dans le worldstate

drones = simu_cfg['drones']
stations = simu_cfg['stations']

for drone in drones:
    battery = Battery(drone["battery"]["maxCycle"], drone["battery"]["lvl"], drone["battery"]["consumption"])
    el = Drone(drone["name"],(drone["homeLocation"]["x"], drone["homeLocation"]["y"]),
               (drone["position"]["x"], drone["position"]["y"]), drone["position"]["z"], drone["failureFrequency"],
               drone["averageSpeed"], battery)
    WorldState.drones.append(el)

for station in stations:
    chargingBatteries = []
    chargedBatteries = []
    for battery in station["chargingBatteries"]:
        chargingBatteries.append(Battery(battery["maxCycle"], battery["lvl"], battery["consumption"]))

    for battery in station["chargedBatteries"]:
        chargedBatteries.append(Battery(battery["maxCycle"],battery["lvl"], battery["consumption"]))

    el = Station(station["name"], (station["position"]["x"], station["position"]["y"]), chargingBatteries,
                 chargedBatteries, station["storageCapacity"], station["chargingTime"], station["chargingSlots"],
                 station["changeDuration"], station["failureFrequency"])
    WorldState.stations.append(el)

r = Renderer(800, 640)
sch = Scheduler()
sch.start()
r.mainloop()
