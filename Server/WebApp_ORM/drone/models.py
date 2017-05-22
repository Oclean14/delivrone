# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from datetime import timezone

from django.db import models

class Customer(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n [name : {0}] \n".format(self.name)

    class Meta:
        managed = True
        db_table = 'customer'

class Drone(models.Model):
    #drone_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    consumption = models.FloatField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=45, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    #dronepos_id = models.ForeignKey(Droneposition, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null= True)
    #dronepos_id = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    #customer_id = models.IntegerField(blank=True, null=True)
    #dronepos_id = models.ForeignKey('Droneposition', models.DO_NOTHING, db_column='dronepos_id', blank=True, null=True)
    #customer_id = models.ForeignKey('Customer', models.DO_NOTHING, db_column='dronePos_id', blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n[status : {0}, height : {1}, comsumption : {2}, name : {3}, radius : {4}, weight : {5}, customer_id : {6} ]".format(self.status, self.height,self.consumption, self.name, self.radius, self.weight, self.customer_id)

    class Meta:
        managed = True
        db_table = 'drone'



class Droneposition(models.Model):
    #dronepos_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    latitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    longitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    altitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    #timestamp_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE, null= True)
    creation_date = models.DateTimeField(auto_now_add=True)
    timestamp_value = models.DateTimeField(auto_now=True)
    #timestamp_value = models.DateTimeField(default=timezone.now)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n[latitude : {0}, longitude : {1}, altitude : {2},creation date : {3},  timestamp : {4}, drone_id : {5}] \n".format(self.latitude, self.longitude,self.altitude, self.creation_date,self.timestamp_value, self.drone_id)

    class Meta:
        managed = True
        db_table = 'droneposition'


class Stock(models.Model):
    #stock_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    longitude = models.FloatField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n[name : {0}, latitude : {1}, longitude : {2}]".format(self.name, self.latitude,self.longitude)


    class Meta:
        managed = True
        db_table = 'stock'



class Delivery(models.Model):
    #mission_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    destinationposlat = models.FloatField(db_column='destinationPosLat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destinationposlon = models.FloatField(db_column='destinationPosLon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE, null= True)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, null= True)
    #drone_id = models.IntegerField(blank=True, null=True)
    #stock_id = models.IntegerField(blank=True, null=True)
    #drone_id = models.ForeignKey('Drone', models.DO_NOTHING, blank=True, null=True)
    #stock_id = models.ForeignKey('Stock', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n[Description : {0}, latitude : {1}, longitude : {2}, drone_id : {3}, stock_id : {4}]".format(self.description, self.destinationposlat,self.destinationposlon, self.drone_id, self.stock_id)


    class Meta:
        managed = True
        db_table = 'delivery'


class Packet(models.Model):
    #packet_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, null= True)
    #stock_id = models.ForeignKey('Stock', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n[status : {0}, stock_id : {1}]".format(self.status, self.stock_id)

    class Meta:
        managed = True
        db_table = 'packet'

class Station(models.Model):
    #id = models.AutoField(primary_key=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n[longitude : {0}, latitude : {1}]".format(self.long, self.lat)

    class Meta:
        managed = True
        db_table = 'Station'


# Unable to inspect table 'charginglog'
# The error was: list index out of range

class Charginglog(models.Model):
    #charginglog_id = models.AutoField(primary_key=True)
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE, null= True)
    drone_id = models.ForeignKey(Drone, on_delete=models.CASCADE, null= True)
    #timestamp_value = models.AutoDateTimeField(default=timezone.now)
    creation_date = models.DateTimeField(auto_now_add=True)
    timestamp_value = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n[Station id : {0}, drone id : {1}, creation date : {2}, timestamp : {3}]".format(self.station_id, self.drone_id, self.creation_date, self.timestamp_value)


    class Meta:
        managed = True
        db_table = 'charginglog'


