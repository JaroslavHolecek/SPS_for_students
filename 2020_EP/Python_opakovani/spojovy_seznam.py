class Prvek:
    def __init__(self, zprava_k_ulozeni):
        self.zprava = zprava_k_ulozeni
        self.dalsi_prvek = None

class Spojovy_seznam():
    def __init__(self):
        self.prvni_prvek = None
        self.posledni_prvek = None

    def pridej_zpravu(self, zprava_k_pridani):
        novy_prvek = Prvek(zprava_k_pridani)
        if self.prvni_prvek is None:
            self.prvni_prvek = novy_prvek
            self.posledni_prvek = novy_prvek
        else:
            self.posledni_prvek.dalsi_prvek = novy_prvek
            self.posledni_prvek = novy_prvek

    def zobraz_seznam(self):
        k_zobrazeni = self.prvni_prvek
        while k_zobrazeni is not None:
            print(k_zobrazeni.zprava)
            k_zobrazeni = k_zobrazeni.dalsi_prvek

muj_seznam = Spojovy_seznam()
seznam_zprav = []

while True:
    zprava = input("Zadej zprávu: ")
    if zprava == "K":
        break

    muj_seznam.pridej_zpravu(zprava)
    seznam_zprav.append(zprava)

print("=======")
muj_seznam.zobraz_seznam()
print("======")
print(seznam_zprav)