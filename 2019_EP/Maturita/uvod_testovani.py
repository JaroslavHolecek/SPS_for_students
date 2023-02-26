import unittest


class TestDeleni(unittest.TestCase):
    def test_deleni(self):
        self.assertEqual(deleni(10,5), 2.0, "Should be 2.0")

    def test_deleni2(self):
        self.assertEqual(deleni(15,5), 3.0, "Should be 3.0")

unittest.main()
# def test_deleni(a,b,vysledek):
#     print(f"deleni(a,b) pro a={a}, b={b} ", end='')
#     nas_vysledek = deleni(a,b)
#     assert nas_vysledek == vysledek, f"KO - vyšlo {nas_vysledek} místo {vysledek}"
#     print("OK")
