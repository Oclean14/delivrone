import random

import sys

from threading import Thread

import time
from .Station import *
from .main import *
class Charger(Thread):


    """Thread"""
    def __init__(self, stationList):
        Thread.__init__(self)
        self.batteryID = batteryID

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""


