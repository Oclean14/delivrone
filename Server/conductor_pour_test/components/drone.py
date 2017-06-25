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


    def registerMission(id,step1, step2, step3):
        missionList.append([id,step1, step2, step3, -1])

    def moveTo(self,destination):
        position[0] = position[0] + speedMean * (destination[0] - position[0])/math.sqrt((destination[1] - position[1])^2 + (destination[0] - position[0])^2)
        position[1] = position[1] + speedMean * (destination[1] - position[1])/math.sqrt((destination[1] - position[1])^2 + (destination[0] - position[0])^2)

    def executeMission(self,id):
        i = 0
        for miss in missionList:
            if miss[0] == id:
                # on passe le statut a 0 = en attente
                missionList[i][4] = 0
            i = i + 1
        i = i - 1

        for j in range(1,3):
            self.moveTo(missionList[i][j])
            time.sleep(5)

        # on passe le statut a effectuee
        missionList[i][4] = 1


