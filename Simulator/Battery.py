import math, random
import time
from Simulator.main import *
id = 0
chargePercentage = 100
chargingCycleDone = 0
maxCycle = 0

class Battery:
    def __init__(self, id, maxCycle):
        self.id = id
        self.maxCycle = maxCycle

    def use(self):
        self.chargePercentage = chargePercentage - consumption

    def getChargePercentage(self):
        return self.chargePercentage
    def charge(self):
        a=0