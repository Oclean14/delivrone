import sqlite3
import random


class Packet() :

    global packet_array;
    packet_array = ["0", "Waiting", "Delivering", "Delivered"];

    def __init__(self, name, status, weight, id_stock):
        self.name = name
        self.status = status
        self.weight = weight
        self.id_stock = id_stock


    @classmethod
    def findAllPackets(self):
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Packet""")
        packets = cursor.fetchall()
        conn.close()
        return packets


    @classmethod
    def FindIdByStatus (self, status):
        status = packet_array.index(status);
        status = str(status);
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT id FROM Packet WHERE status=\'"""+ status + """\'""")
        packets = cursor.fetchall()
        conn.close()
        return packets

    def save(self):
        self.status = packet_array.index(self.status);
        self.status = str(self.status);
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        print("Opened database successfully");
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Packet (name, packetWeight, stock_id_id, status) \
    VALUES (\'" + self.name + "\', \'" + self.weight + "\' , \'" + self.id_stock+ "\' , \'" + self.status+ "\')");
        conn.commit()
        cursor.close()
        print("Operation done successfully");

    #It will create random paquet in random existing station
    @classmethod
    def saveRandom(self, number):
        for x in range(0, number):
            k = random.randint(2,9)
            paquet = Packet("packet" + str(x * random.random()), "Waiting", "3", str(k))
            paquet.save()

    @classmethod
    def UpdateStatusById (self, id, status):
        status = packet_array.index(status);
        status = str(status);
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        print("Opened database successfully");
        cursor = conn.cursor()
        # cursor.execute("UPDATE Delivery SET status=\'"+ status + "\' WHERE id=\'" + id + "\'");
        cursor.execute("UPDATE Packet SET status=? WHERE id=?", (status, id));
        conn.commit()
        cursor.close()
        print("Operation done successfully");

    def getName(self):
            return self.name

    def getWeight(self):
            return self.weight

    def getStatus(self):
            return self.status

    def getStockId(self):
            return self.id_stock


    def setName(self, name):
        self.name = name

    def setWeight(self, weight):
        self.weight = weight

    def setStatus(self, status):
            self.status = status

    def setStockId(self, id_stock):
            self.id_stock = id_stock