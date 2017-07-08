import unittest
from utils import *

class UtilsTestMethods(unittest.TestCase):

    def test_dist(self):
        v1 = (0, 0)
        v2 = (6, 0)
        self.assertEqual(dist(v1, v2), 6)

if __name__ == '__main__':
    unittest.main()
