from threading import Thread

class BatteryChangerThread(Thread):
        def __init__(self,associatedStation):
            Thread.__init__(self)
            self.associatedStation = associatedStation






