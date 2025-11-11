import unittest

def faktorialx(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n*faktorialx(n-1)

class TestFaktorial(unittest.TestCase):

    def test_faktorial(self):
        self.assertEqual( 120, faktorialx(5))

    def test_faktorial1(self):
        self.assertEqual( 2, faktorialx(2))

    def test_faktorial2(self):
        self.assertEqual( 6,faktorialx(3) )

    def test_faktorial3(self):
        self.assertEqual(1, faktorialx(0))

    def test_faktorial4(self):
        self.assertEqual(15511210043330985984000000, faktorialx(25))

    def test_faktorial5(self):
        self.assertEqual(None, faktorialx(-4))


    # def test_create_square_negative_length(self):
    #     with self.assertRaises(ValueError):
    #         pass# square = Square(-1)

    # def test_square_instance_of_shape(self):
    #     pass# self.assertIsInstance(square, Shape)

if __name__ == '__main__':
    unittest.main()