from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Stock)
admin.site.register(Droneposition)
admin.site.register(Drone)
admin.site.register(Delivery)
admin.site.register(Packet)
admin.site.register(Station)
admin.site.register(Charginglog)