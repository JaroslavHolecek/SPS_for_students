# Unit testy pro funkci secti
import unittest
import bubblesort

bubblesort.bubble()

# Funkce pro sčítání dvou čísel
def secti(a, b):
    return a + b

class TestSectiFunkce(unittest.TestCase):

    def test_soucet_kladnych_cisel(self):
        self.assertEqual(secti(2, 0), 2)  # Očekáváme, že 2 + 3 bude 5

    def test_soucet_zapornych_cisel(self):
        self.assertEqual(secti(-2, -3), -5)  # Očekáváme, že (-2) + (-3) bude -5

    def test_soucet_kladneho_a_zaporneho_cisla(self):
        self.assertEqual(secti(5, -3), 2)  # Očekáváme, že 5 + (-3) bude 2

    def test_soucet_nuly_a_kladneho_cisla(self):
        self.assertEqual(secti(0, 7), 7)  # Očekáváme, že 0 + 7 bude 7

if __name__ == '__main__':
    unittest.main()
