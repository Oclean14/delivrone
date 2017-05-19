# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n id :{0} [name : {1}] \n".format(self.id, self.name)

    class Meta:
        managed = False
        db_table = 'customer'


class Droneposition(models.Model):
    latitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    longitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    altitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    timestamp_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    #timestamp_value = models.TimeField(blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n id : {0} [latitude : {1}, longitude : {2}, altitude : {3}, timestamp : {4}] \n".format(self.dronepos_id, self.latitude, self.longitude,self.altitude, self.timestamp_value)

    class Meta:
        managed = False
        db_table = 'droneposition'


class Drone(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    consumption = models.FloatField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=45, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    dronepos_id = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(blank=True, null=True)
    #dronepos_id = models.ForeignKey('Droneposition', models.DO_NOTHING, db_column='dronepos_id', blank=True, null=True)
    #customer_id = models.ForeignKey('Customer', models.DO_NOTHING, db_column='dronePos_id', blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n id : {0} [status : {1}, height : {2}, comsumption : {3}, name : {4}, radius : {5}, weight : {6}, dronePos_Id : {7}, customer_id : {8} ]".format(self.drone_id, self.status, self.height,self.consumption, self.name, self.radius, self.weight, self.dronepos_id, self.customer_id)

    class Meta:
        managed = False
        db_table = 'drone'


class Stock(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    longitude = models.FloatField(blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n id : {0} [name : {1}, latitude : {2}, longitude : {3}]".format(self.stock_id, self.name, self.latitude,self.longitude)


    class Meta:
        managed = False
        db_table = 'stock'



class Delivery(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    destinationposlat = models.FloatField(db_column='destinationPosLat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destinationposlon = models.FloatField(db_column='destinationPosLon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    drone_id = models.IntegerField(blank=True, null=True)
    stock_id = models.IntegerField(blank=True, null=True)
    #drone_id = models.ForeignKey('Drone', models.DO_NOTHING, blank=True, null=True)
    #stock_id = models.ForeignKey('Stock', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n id : {0} [Description : {1}, latitude : {2}, longitude : {3}, drone_id : {4}, stock_id : {5}]".format(self.mission_id, self.description, self.destinationposlat,self.destinationposlon, self.drone_id, self.stock_id)


    class Meta:
        managed = False
        db_table = 'delivery'


class Packet(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    stock_id = models.IntegerField(blank=True, null=True)
    #stock_id = models.ForeignKey('Stock', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n id : {0} [status : {1}, stock_id : {2}]".format(self.packet_id, self.status, self.stock_id)

    class Meta:
        managed = False
        db_table = 'packet'

class Station(models.Model):
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n id : {0} [longitude : {1}, latitude : {2}]".format(self.id, self.long, self.lat)

    class Meta:
        managed = False
        db_table = 'Station'


# Unable to inspect table 'charginglog'
# The error was: list index out of range

class Charginglog(models.Model):
    station_id = models.IntegerField(blank=True, null=True)
    drone_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        #return u'%d %s' % (self.id,self.name)
        return "\n id : {0} [status : {1}, stock_id : {2}]".format(self.charginglog_id, self.station_id, self.drone_id)


    class Meta:
        managed = False
        db_table = 'charginglog'


