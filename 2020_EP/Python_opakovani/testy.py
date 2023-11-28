import unittest
import math

def obvod_kruhu(r):
    if r >= 0:
        return 2*math.pi*r
    else:
        return None

class Test(unittest.TestCase):

    def test_obvod(self):
        self.assertEqual(2*math.pi*1, obvod_kruhu(1))

    def test_obvod_nula(self):
        self.assertEqual(0, obvod_kruhu(0))

    def test_obvod_zaporny(self):
        self.assertEqual(None, obvod_kruhu(-10))

    # def test_create_square_negative_length(self):
    #     with self.assertRaises(ValueError):
    #         pass# square = Square(-1)

    # def test_square_instance_of_shape(self):
    #     pass# self.assertIsInstance(square, Shape)



if __name__ == '__main__':
    unittest.main()