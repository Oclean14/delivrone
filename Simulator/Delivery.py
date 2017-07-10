# -*- coding: utf-8 -*-
""" Classe definissant une delivery (mission) caracterisee par :"""
#- son nom
#- la position de destination
#- l'id du drone auquel est affecte la mission courante
#- l'id du stock d'ou vient le colis
#- l'id du colis
#- le statut de la mission

# Etat de la livraison
import time

class Delivery:
    __id = 0
    NOT_STARTED = 0
    STARTED = 1
    ABORTED = 2
    FINISHED = 3

    def __init__(self, name, packet, path):
        self.name = name
        self.status = Delivery.NOT_STARTED
        self.id = Delivery.__id + 1
        self.packet = packet
        self.path = path
        self.timestamp = time.time()
