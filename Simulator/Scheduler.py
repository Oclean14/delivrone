# -*- coding: utf-8 -*-
from time import sleep
from Delivery import *
from Drone import *
from Packet import *
from WorldObjects import WorldObjects as ws
from threading import Thread
from Log import Log as l
from drone_state import DroneState
from parametersModel import *
from utils import dist
global i


def deliveryActivity(drone, delivery):
    drone.start()
    drone.takeoff(1,1)
    drone.executeDelivery(delivery)

class Scheduler:
    FREQ_GEN_DELIVERY = 2
    TAG = "SCHEDULER"
    def __init__(self):
        self.deliveries = []

    def start(self):
        runThread = Thread(target=self.run, args=())
        deliveryThread = Thread(target=self.generateDelivery, args=())
        runThread.daemon = True                            # Daemonize thread
        deliveryThread.daemon = True
        runThread.start()
        deliveryThread.start()

    def generateDelivery(self):
        while True:
            print "Generate delivery"
            path = []
            weight = random.uniform(1.5, 3.2)
            x = random.randint(50, 800)
            y = random.randint(50, 640)
            path.append((x,y))
            name = "delivery"
            packet = Packet(name, weight)
            delivery = Delivery(name, packet, path)
            self.deliveries.append(delivery)
            sleep(Scheduler.FREQ_GEN_DELIVERY * oneSecond)

    def predict(self, drone,destPoint, time):
        vecDir = vec2d_normalize(vec2d_sub(destPoint, drone.position))
        vecDir = vec2d_multiply_scalar(vecDir, drone.velocity)
        predictPosition = vec2d_add(drone.position, vec2d_multiply_scalar(vecDir, time / Drone.MOVE_UPDATE_FREQ))
        predictBat =  drone.battery.chargePercentage - ((Drone.CONSUME_BATTERY_FREQ / time) * drone.battery.consumption)
        return (predictPosition, predictBat)

    def run(self):
        while True:
            jobs = []
            sleep(Scheduler.FREQ_GEN_DELIVERY * oneSecond)
            if self.deliveries:
                    delivery = self.deliveries.pop()
                    drone = self.chooseDroneToExecuteMission(delivery.path[0])
                    print str(self.predict(drone ,delivery.path[0],  10))
                    job = Thread(target=deliveryActivity, args=(drone, delivery))
                    jobs.append(job)

            for job in jobs:
                job.start()

    def chooseDroneToExecuteMission(self, destPoint):
        noteDroneActuel=0.0
        noteDronePrecedent=0.0
        choosedDrone=ws.drones[0]
        for drone in ws.drones:
            if not drone.state & DroneState.DELYVERING:
                noteDroneActuel = drone.battery.chargePercentage / dist(drone.position, destPoint)
                if noteDroneActuel > noteDronePrecedent:
                    choosedDrone = drone
        return choosedDrone

    def getRegularlyMissions(self):
        print("We are going to retrieve all NOT STARTED delivery every 20 seconds")
        sleep(20)
        mission = Delivery.findByStatus("NOT STARTED")
        return mission

    @classmethod
    def randomAssignMission (self, frequency) :
        time = 1
        if frequency != time :
            print("We are going to wait for" + str(time *frequency) + "seconds" )
            sleep(time * frequency)
        else :
            print("We are going to wait for" + str(time) + "seconds")
            sleep(time)

        packets = Packet.FindIdByStatus("Waiting");
        print(packets)
        packetList = []

        for packet in packets:
            print(packet[0])
            #i = 6;
            #i = i + 1;
            j = str(random.randint(1,100));
            print("for packet id :" + str(packet[0]) + " we are going to create the delivery : delivery" + j)
            print("We will first search a free drone :")
            drone_id = "0";
            drones = Drone.FindIdByStatus("STANDBY")
            if len(drones) >= 1 :
                #print(" Hello this the lend :"+str(len(drones)))
                print("VOILA LE DRONE ID " + str(drones[0][0]))
                mission = Delivery("delivery" + j, "55", str(drones[0][0]), "2", str(packet[0]), "NOT STARTED");
                mission.save()
                drone = Drone.UpdateStatusByID(str(drones[0][0]), "ACTIVE")
                Packet.UpdateStatusById(str(packet[0]), "Delivering")
                #print("we are going to assign this mission to drone id :" + str(drones[0][0]))
                #for drone in drones:
                    #drone_id = drone[0]
                    #drone_id = str(drone_id);
                    #print("we are going to assign this mission to drone id :" + str(drones[0][0]))
                    #goto end
            else :
                print("Il n'y plus de drone dispo, on rajoute le packet e la queue")
                packetList.append(packet)
                Packet.UpdateStatusById(str(packet[0]),"Delivering")
                print(packetList)

        return packetList
