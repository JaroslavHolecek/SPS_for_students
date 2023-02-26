import unittest
from my_deleni import deleni # deleni

class TestDeleni(unittest.TestCase):
    def test_deleni(self):
        self.assertEqual(deleni(10,5), 2.0, "Should be 2.0")

    def test_deleni2(self):
        self.assertEqual(deleni(15,5), 3.0, "Should be 3.0")
    def test_deleni_0(self):
        self.assertEqual(deleni(15,0), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()