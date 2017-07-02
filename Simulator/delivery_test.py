from Simulator.Packet import *
from Simulator.Delivery import *


#packet = Packet("TOTO", "Waiting", "15","2");
#packet.save();

packets = Packet.FindIdByStatus("Waiting");
print(packets)
packetList = []
i = 6;
for packet in packets:
 print(packet[0])
 i = i + 1;
 j = str(i);
 print("for packet id :" + str(packet[0]) +" we are goign to create the delivery : delivery" + j)
 mission = Delivery("delivery" + j, "55", "1", "", "2", "NOT STARTED");
 mission.save()
