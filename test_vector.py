import unittest
from myVector import Point, Vector

class Test_Vector(unittest.TestCase):
    def test_Point(self):
        test_p = Point(2,4)
        self.assertEqual(test_p + 3, Point(5,7))
        pass
    def test_Vector(self):
        test_v = Vector((0,0), (2,2))
        test_v1 = Vector((0,0), (2,-2))
        self.assertEqual(test_v.reverseByXAxis(), test_v1)
        pass 