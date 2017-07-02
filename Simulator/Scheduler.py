from time import sleep
from Simulator.Delivery import *

class Scheduler() :

    def getRegularlyMissions(self):
        print("We are going to retrieve all NOT STARTED delivery every 20 seconds")
        sleep(20)
        mission = Delivery.findByStatus("NOT STARTED")
        return mission

    def randomAssignMission (self, frequency) :
        print("HELLO WORLD")