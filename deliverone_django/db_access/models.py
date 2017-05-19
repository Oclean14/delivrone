"""from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)"""

from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)


class Droneposition(models.Model):
    latitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    longitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    altitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    timestamp_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    #timestamp_value = models.TimeField(blank=True, null=True)




class Drone(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    consumption = models.FloatField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=45, blank=True, null=True)
    radius = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    #dronepos_id = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    #customer_id = models.IntegerField(blank=True, null=True)
    #dronepos_id = models.ForeignKey('Droneposition', models.DO_NOTHING, db_column='dronepos_id', blank=True, null=True)
    #customer_id = models.ForeignKey('Customer', models.DO_NOTHING, db_column='dronePos_id', blank=True, null=True)



class Stock(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)  # This field type is a guess.
    longitude = models.FloatField(blank=True, null=True)  # This field type is a guess.




class Delivery(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    destinationposlat = models.FloatField(db_column='destinationPosLat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destinationposlon = models.FloatField(db_column='destinationPosLon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
   # drone_id = models.IntegerField(blank=True, null=True)
   # stock_id = models.IntegerField(blank=True, null=True)
    #drone_id = models.ForeignKey('Drone', models.DO_NOTHING, blank=True, null=True)
    #stock_id = models.ForeignKey('Stock', models.DO_NOTHING, blank=True, null=True)




class Packet(models.Model):
    status = models.CharField(max_length=255, blank=True, null=True)
    stock_id = models.IntegerField(blank=True, null=True)
    #stock_id = models.ForeignKey('Stock', models.DO_NOTHING, blank=True, null=True)

class Station(models.Model):
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)


class Charginglog(models.Model):
    station_id = models.IntegerField(blank=True, null=True)
    drone_id = models.IntegerField(blank=True, null=True)




