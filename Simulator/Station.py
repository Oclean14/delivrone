import math, random
import time
from .Battery import *

inGarbage = 0
batteryList = []
position = []
numberBattery = 0
speedOfCharge = 0
timeOfChange = 0
maxCycle = 0

class Station:
    def __init__(self, id, position, numberBattery, speedOfCharge, timeOfChange, maxCycle):
        self.id = id
        self.position = position
        self.numberBattery = numberBattery
        self.speedOfCharge = speedOfCharge
        self.timeOfChange = timeOfChange
        self.maxCycle = maxCycle

    def createStock(self):
        for i in range(0,numberBattery):
            batteryList.append(Battery())




