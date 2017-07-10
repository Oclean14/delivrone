"""Ce fichier permet de renseigner tous les parametres"""
#Aerianspace

aerianSpace = []

#Drone

numberDrone = 100
averageSpeed = 10
failureFrequency = 0.1 #panne/heure de vol/drone

#Station

numberStation = 10
batteriesPerStation = 20
chargingTime = 3 #(pourcentage de accumule par minute)
changingTime = 60 #(nombre de seconde pour le changement de batterie)

#Delivery

mode = 1 # 0 : utilisation des missions du site uniquement, 1 : mode auto, 2 : mode hybride
deliveryFrequency = 2 #frequence de creation de mission par minute


#Batterie

consumption = 3 # consommation en pourcentage de batterie par minute en vol pour simplifier
maxCycle = 300 # nombre de cycle de rechargement des batteries

#Time
startAt = "100416052000"
oneSecond = 0.0001

#Stock in Warehouse
motorsNumber = 60
motorPrice = 100 #euro
propellersNumber = 100
propellerPrice = 30

stationList = []
droneList = []
WarehouseList = []
