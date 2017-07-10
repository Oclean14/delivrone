# -*- coding: utf-8 -*-
from time import sleep
from Delivery import *
from Drone import *
from Packet import *
from WorldObjects import WorldObjects as ws
from threading import Thread
from Log import Log as l
from drone_state import DroneState
global i


def move_drone(drone, delivery):
    print "move drone"
    drone.start()
    drone.takeoff(1,1)
    drone.executeDelivery(delivery)

class Scheduler:

    TAG = "SCHEDULER"

    def start(self):
        thread = Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()

    def run(self):
        jobs = []
        for drone in ws.drones:
            if not drone.state & DroneState.DELYVERING:
                #test
                path = []
                w = random.randint(1, 3)
                for i in range(0, 4):
                    x = random.randint(50, 800)
                    y = random.randint(50, 640)
                    path.append((x,y))
                l.debug(Scheduler.TAG, str(path))
                name = "delivery"
                packet = Packet(name, w)
                delivery = Delivery(name, packet, path)

                thread = Thread(target=move_drone, args=(drone, delivery))
                jobs.append(thread)

        for job in jobs:
            job.start()

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
