from Simulator.Packet import *
from Simulator.Delivery import *
from Simulator.Drone import *
from Simulator.Scheduler import *
from Simulator.Packet import *

#global drone_id;
#packet = Packet("TOTO", "Waiting", "15","2");
#packet.save();

"""packets = Packet.FindIdByStatus("Waiting");
print(packets)
packetList = []
i = 6;
for packet in packets:
 print(packet[0])
 i = i + 1;
 j = str(i);
 print("for packet id :" + str(packet[0]) +" we are going to create the delivery : delivery" + j)
 print("We will first search a free drone :")
 drone_id = "0";

 drones = Drone.FindIdByStatus("STANDBY")
 for drone in drones:
     drone_id = drone[0]
     drone_id = str(drone_id);
     print("we are going to assign this mission to drone id :" + str(drone_id))
     break

 print("VOILA LE DRONE ID " + drone_id)
 mission = Delivery("delivery" + j, "55", drone_id, "2", str(packet[0]),"NOT STARTED");
 mission.save()
 drone = Drone.UpdateStatusByID(drone_id, "ACTIVE")"""

packet = Packet.saveRandom(20)
while (True) :
    #packet = Packet.saveRandom(20)
    left_packet = Scheduler.randomAssignMission(5);
    #print("This is the list for which one we need to create missions")
    #print(left_packet)
    #break;

#drone = Drone.FindIdByStatus("POWEROFF")
#print(str(len(drone)))