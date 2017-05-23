from __future__ import unicode_literals
# install django-multiselectfield
from multiselectfield import MultiSelectField

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "\n Nom : {0}\n".format(self.name)

    class Meta:
        managed = True
        db_table = 'customer'

# Status du drone. En recopiant les l'attribut system_status de l'objet vehicule cree
STATUS_drone = ((1, 'UNINIT'),
          (2, 'BOOT'),
          (3, 'CALIBRATING'),
          (4, 'STANDBY'),
          (5, 'ACTIVE'),
		  (6, 'CRITICAL'),
		  (7, 'EMERGENCY'),
		  (8, 'POWEROFF'))

# Etat de la livraison		  
STATUS_delivery = ((1, 'NOT STARTED'),
          (2, 'STARTED'),
          (3, 'ABORTED'),
          (4, 'FINISHED'))

class Drone(models.Model):
    status = MultiSelectField(choices=STATUS_drone,
                                 max_choices=1, null=True)
    height = models.IntegerField(blank=True, null=True)
    consumption = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return "\n Nom : {0}, Statut : {1}, Client : {2}".format(self.name, self.status, self.customer_id)

    class Meta:
        managed = True
        db_table = 'drone'



class Droneposition(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE, null= True)
    creation_date = models.DateTimeField(auto_now_add=True)
    timestamp_value = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "\n Drone : {0}, Latitude : {1}, Longitude : {2}, Altitude : {3}, Timestamp : {4}\n".format(self.drone_id, self.latitude, self.longitude,self.altitude, self.timestamp_value)

    class Meta:
        managed = True
        db_table = 'droneposition'


class Stock(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    longitude = models.FloatField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return "\n Name : {0}".format(self.name)
    class Meta:
        managed = True
        db_table = 'stock'


STATUS_packet = ((1, 'Au Stock'),
                 (2, 'En Livraison'),
                 (3, 'Pas disponible'))

class Packet(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    status = MultiSelectField(choices=STATUS_packet,
                                 max_choices=1, null=True)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return "\n Code : {0}, Statut : {1}, Stock : {2}]".format(self.name, self.status, self.stock_id)

    class Meta:
        managed = True
        db_table = 'packet'

class Delivery(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    destinationposlat = models.FloatField(db_column='destinationPosLat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destinationposlon = models.FloatField(db_column='destinationPosLon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE, null= True)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, null= True)
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, null=True)
    status = MultiSelectField(choices=STATUS_delivery, max_choices=1, null=True)
	
    def __str__(self):
        return "\nTitre : {0}, Description : {1}, Drone : {2}, Stock : {3}, Produit : {4}".format(self.name, self.description, self.drone_id, self.stock_id, self.packet)
    class Meta:
        managed = True
        db_table = 'delivery'

class Station(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    num_charged_battery = models.IntegerField(blank=True, null=True)
    anticipated_charged_battery = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "\nNom : {0}, Longitude : {1}, Latitude : {2}, Nombre de batteries chargées : {3}".format(self.name, self.long, self.lat, self.num_charged_battery)

    class Meta:
        managed = True
        db_table = 'Station'


class Charginglog(models.Model):
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE, null= True)
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE, null= True)
    creation_date = models.DateTimeField(auto_now_add=True)
    timestamp_value = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "\n Drone : {0}, Station : {1}, Date de création : {2}, Timestamp : {3}".format(self.drone_id, self.station_id, self.creation_date, self.timestamp_value)

    class Meta:
        managed = True
        db_table = 'charginglog'


