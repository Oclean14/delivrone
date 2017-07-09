# -*- coding: utf-8 -*-
import sqlite3

class Delivery() :

    """ Classe définissant une delivery (mission) caractérisée par :"""
    #- son nom
    #- la position de destination
    #- l'id du drone auquel est affecté la mission courante
    #- l'id du stock d'ou vient le colis
    #- l'id du colis
    #- le statut de la mission

    # Etat de la livraison
    STATUS_delivery = ((1, 'NOT STARTED'),
                       (2, 'STARTED'),
                       (3, 'ABORTED'),
                       (4, 'FINISHED'))

    global delivery_array;
    delivery_array = ["0", "NOT STARTED", "STARTED", "ABORTED", "FINISHED"];

    def __init__(self, name, position, id_drone, id_stock, id_colis, status):
        self.name = name
        self.position = position
        self.status = status
        self.id_stock = id_stock
        self.id_colis = id_colis
        self.id_drone = id_drone

    @classmethod
    def getAllDeliveries(self):
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Delivery""")
        missions = cursor.fetchall()
        conn.close()
        return missions

    @classmethod
    def findByName(self, name):
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Delivery WHERE name=\'""" + name + """\'""")
        mission = cursor.fetchall()
        conn.close()
        return mission

    @classmethod
    def findByStatus(self, status):
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        cursor = conn.cursor()
        value = delivery_array.index(status);
        value = str(value);
        cursor.execute("""SELECT * FROM Delivery WHERE status=\'""" + value + """\'""")
        mission = cursor.fetchall()
        conn.close()
        return mission

    @classmethod
    def findBy(self,colonne, value):
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Delivery WHERE """ + colonne +"""=\'""" + value + """\'""")
        mission = cursor.fetchall()
        conn.close()
        return mission

    def save (self):
        self.status = delivery_array.index(self.status);
        self.status = str(self.status);
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        print("Opened database successfully");
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Delivery (name, position, status, drone_id_id, stock_id_id, packet_id) \
 VALUES (\'" + self.name +"\', \'"+ self.position +"\' , \'" + self.status + "\' , \'" + self.id_drone + "\' , \'"  + self.id_stock + "\', \'"+ self.id_colis+"\' )");
        conn.commit()
        cursor.close()
        print("Operation done successfully");

    @classmethod
    def updateStatusByID(self ,id, status):
            status = delivery_array.index(status);
            status = str(status);
            conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
            print("Opened database successfully");
            cursor = conn.cursor()
            #cursor.execute("UPDATE Delivery SET status=\'"+ status + "\' WHERE id=\'" + id + "\'");
            cursor.execute("UPDATE Delivery SET status=? WHERE id=?", (status, id));
            conn.commit()
            cursor.close()
            print("Operation done successfully");


    #GET and SET methods
        ##
        #	Recupere l'etat du delivery
    def getName(self):
            return self.name

    def getPosition(self):
            return self.position

    def getStatus(self):
            return self.status

    def getDroneId(self):
            return self.id_drone

    def getStockId(self):
            return self.id_stock

    def getPacketId(self):
            return self.id_colis

        ##
        #	Renseigne l'etat du delivery
    def setName(self, name):
        self.name = name

    def setPosition(self, position):
        self.position = position

    def setStatus(self, status):
            self.status = status

    def setDroneId(self, id_drone):
        self.id_drone = id_drone

    def setStockId(self, id_stock):
        self.id_stock = id_stock

    def setPacketId(self, id_colis):
        self.id_colis = id_colis
