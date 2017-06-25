import math, random
import time
from .Battery import *


position = []
missionList = []
speedMean = 50
battery = Battery
class Drone :

    def __init__(self, id, defaultPosition):
        self.id = id
        self.position = defaultPosition
        self.status = "free"

