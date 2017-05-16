import math, random
import time
position = [0,0]
missionList = []
speedMean = 50
class Drone :
    def __init__(self, id, defaultPosition):
        self.id = id
        self.position = defaultPosition
        self.status = "free"


    def registerMission(id,stationCoords, stockCoords, destinationCoords, state):
        missionList.append([id,stationCoords, stockCoords, destinationCoords, state])

    def moveTo(self,destination):
        position[0] = position[0] + speedMean * (destination[0] - position[0])/math.sqrt((destination[1] - position[1])^2 + (destination[0] - position[0])^2)
        position[1] = position[1] + speedMean * (destination[1] - position[1])/math.sqrt((destination[1] - position[1])^2 + (destination[0] - position[0])^2)

    def executeMission(self,id):
        i = 0
        for miss in missionList:
            if miss[0] == id:
                missionList[i][4] = 0
            i = i + 1
        stockPosition = missionList[i][2]
        destinationPosition = missionList[i][3]
        self.moveTo(stockPosition)
        time.sleep(5)
        self.moveTo(destinationPosition)
        time.sleep(5)


    def nextMissionId(self):


    def run(self):

