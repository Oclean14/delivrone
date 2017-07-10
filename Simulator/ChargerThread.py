import random
import sys
from threading import Thread
import time
import parametersModel

class Charger(Thread):
    """Thread"""

    def __init__(self, associatedStation):
        Thread.__init__(self)
        self.associatedStation = associatedStation

    def run(self):
        while True:
            for battery in self.associatedStation.batteryList:
                if battery.getChargePercentage() <= 100 and battery.isUsable():
                    battery.charge(chargingTime)
                if not battery.isUsable():
                    self.associatedStation.unusableBatteryList.append(battery)
            time.sleep(60 * oneSecond)
