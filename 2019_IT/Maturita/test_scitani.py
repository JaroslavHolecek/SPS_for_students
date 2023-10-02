import unittest
import scitani

class TestScitani(unittest.TestCase):
    def test_scitani(self):
        self.assertEqual(scitani.scitani_tri(10,5, 0), 15, "Should be 15")
    def test_scitani2(self):
        self.assertEqual(scitani.scitani_tri(10,5, 1), 16, "Should be 16")
    def test_scitani0(self):
        self.assertEqual(scitani.scitani_tri(15,5, -5), 15, "Should be 15")

if __name__ == '__main__':
    unittest.main()

