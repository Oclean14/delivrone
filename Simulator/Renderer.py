# -*- coding: utf-8 -*-
import Tkinter as tk
import math, random
from WorldObjects import WorldObjects

DRONE_RADIUS = 10
STATION_RADIUS = 15

class Renderer(tk.Tk):
    def __init__(self, canevasW, canevasH):
        tk.Tk.__init__(self)
        self.canevas = tk.Canvas(self, height=canevasH, width=canevasW)
        self.canevas.pack()
        self.updateCanevas()

    def updateCanevas(self):
        self.canevas.delete("all")
        for drone in WorldObjects.drones:
            self.canevas.create_text(drone.position[0], drone.position[1] - 27, anchor=tk.CENTER, font=("Purisa", 9),text=drone.id)
            self.canevas.create_oval(drone.position[0] - DRONE_RADIUS, drone.position[1] - DRONE_RADIUS, drone.position[0] + DRONE_RADIUS, drone.position[1] + DRONE_RADIUS, outline="black", fill="blue", width=2)
        for station in WorldObjects.stations:
            self.canevas.create_text(station.position[0], station.position[1] - 27, anchor=tk.CENTER, font=("Purisa", 9),text=station.id)
            self.canevas.create_rectangle(station.position[0] - STATION_RADIUS, station.position[1] - STATION_RADIUS, station.position[0] + STATION_RADIUS, station.position[1] + STATION_RADIUS, outline="black", fill="red", width=2)
        self.after(50, self.updateCanevas)
