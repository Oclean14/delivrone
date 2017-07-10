import json
from pprint import pprint
from Log import Log as log
from WorldObjects import WorldObjects
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

# Ajout des objets dans le worldstate

drones = simu_cfg['drones']
stations = simu_cfg['stations']

for drone in drones:
    battery = Battery(drone["battery"]["maxCycle"], drone["battery"]["lvl"], drone["battery"]["consumption"])
    el = Drone(drone["name"],(drone["homeLocation"]["x"], drone["homeLocation"]["y"]),
               (drone["position"]["x"], drone["position"]["y"]), drone["position"]["z"], drone["failureFrequency"],
               drone["averageSpeed"], battery)
    WorldObjects.drones.append(el)

for station in stations:
    chargingBatteries = []
    chargedBatteries = []
    for battery in station["chargingBatteries"]:
        chargingBatteries.append(Battery(battery["maxCycle"], battery["lvl"], battery["consumption"]))

    for battery in station["chargedBatteries"]:
        chargedBatteries.append(Battery(battery["maxCycle"],battery["lvl"], battery["consumption"]))

    el = Station(station["name"], (station["position"]["x"], station["position"]["y"]), chargedBatteries, station["storageCapacity"], station["chargingTime"], station["chargingSlots"], station["changeDuration"], station["failureFrequency"])
    WorldObjects.stations.append(el)

r = Renderer(800, 640)
sch = Scheduler()
sch.start()
r.mainloop()
