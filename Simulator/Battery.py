import math, random
import time


class Battery:
    def __init__(self, id, maxCycle):
        self.id = id
        self.chargePercentage = 100
        self.chargingCycle = maxCycle

