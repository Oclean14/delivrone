#import du modele permettant de recuperer les livraisons

from Server.WebApp_ORM.drone.models import Delivery

class Mission:
    def __init__(self):
        lstAllMissions = Delivery.objects.all()

