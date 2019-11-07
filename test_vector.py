import unittest
from vector import Point, Vector

class Test_Vector(unittest.TestCase):
    def test_Point(self):
        test_p = Point(2,4)
        self.assertEqual(test_p + 3, Point(5,7))
        pass
    def test_Vector(self):
        pass