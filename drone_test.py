import unittest
from Drone import Drone
from Battery import Battery

class DroneTestMethods(unittest.TestCase):

    def test_start_stop(self):
        drone = Drone(5, (10,20), (10,20,0), 0.2, (0,0), Battery(300,100,3))
        self.assertEqual(drone.start(), 0)
        self.assertEqual(drone.start(), -1)
        self.assertEqual(drone.stop(), 0)
        self.assertEqual(drone.stop(), -1)

if __name__ == '__main__':
    unittest.main()
