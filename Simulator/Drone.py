import math, random
import time
from Simulator.Battery import *
from threading import Thread

position = []
missionList = []
speedMean = 8 #km/h
battery = Battery
direction = []
startingPosition = position
deliveryList = []

class Drone(Thread) :

    def __init__(self, id, defaultPosition):
        Thread.__init__(self)
        self.id = id
        self.position = defaultPosition
        self.startingPosition = defaultPosition
        self.status = "free"

    def square(self,x):
        return x * x

    def run(self):

        while not(self.isOnTopOfDirection()):
            print("I'm at", self.position, " and I'm going to ", self.direction)
            #if(self.status == "stopped"):
              #  self.startingPosition = position

            distance = math.sqrt(self.square(self.direction[0] - self.startingPosition[0]) + self.square(self.direction[1] - self.startingPosition[1]))
            speedVector = [(speedMean * (self.direction[0] - self.startingPosition[0])/distance), (speedMean * (self.direction[1] - self.startingPosition[1])/distance)]
            self.position[0] = self.position[0] + speedVector[0]
            self.position[1] = self.position[1] + speedVector[1]
            #position[] = position[]
            print("I'm at",self.position," and I'm going to ",self.direction)
            time.sleep(1)

    def setDirection(self, direction):
        self.direction = direction

    def addDelivery(self,delivery):
        self.deliveryList.append(delivery)

    def executeDelivery(self, delivery):
        for pos in delivery:
            i = 1


    def getChargeLevel(self):
        a=0

    def getStatus(self):
        return
    def setStatus(self):
        return
    def getDirection(self):
        return self.direction

    def followPoints(self):#suit les points fournit par un éventuelle calculateur de vol
        a = 0

    def isOnTopOfDirection(self):
        distance = math.sqrt(self.square(self.direction[0] - self.position[0]) + self.square(self.direction[1] - self.position[1]))
        print(distance)
        if(distance > 3):
            return False
        else:
            return True


