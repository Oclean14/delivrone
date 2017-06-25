import sqlite3

class Delivery:

    def getDeliveries(self):
        conn = sqlite3.connect('..\Server\WebApp_ORM\drone.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM Delivery""")
        missions = cursor.fetchall()
        print(missions)