class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def hraj(self):
        return True

class Kolo:
    def __init__(self, pocet_tahu, hrac0, hrac1):
        self.pocet_tahu = pocet_tahu
        self.hrac0 = hrac0
        self.hrac1 = hrac1
        self.body = [0, 0]
        self.vysledky = [] # [ (T,T), (F,T), (F,F), ... ]

    def zahraj_tah(self):
        vysledek0 = self.hrac0.hraj()
        vysledek1 = self.hrac1.hraj()
        self.vysledky.append( (vysledek0, vysledek1) )

        if vysledek0 and vysledek1:
            self.body[0] += 3
            self.body[1] += 3
        elif vysledek0 and not vysledek1:
            self.body[0] += 0
            self.body[1] += 5
        elif not vysledek0 and vysledek1:
            self.body[0] += 5
            self.body[1] += 0
        else:
            self.body[0] += 1
            self.body[1] += 1

        return (vysledek0, vysledek1)

    def odehraj_kolo(self):
        for i in range(self.pocet_tahu):
            self.zahraj_tah()

        return self.body

class Turnaj:
    def __init__(self, vsichni_hraci):
        self.vsichni_hraci = vsichni_hraci
        self.body_hracu = [0] * len(self.vsichni_hraci)
        self.vsechna_kola = []


    def spust_kolo(self, pocet_tahu, index_hrace0, index_hrace1):
        kolo = Kolo(pocet_tahu,
                    self.vsichni_hraci[index_hrace0],
                    self.vsichni_hraci[index_hrace1])

        body_z_kola = kolo.odehraj_kolo()
        if index_hrace0 == index_hrace1:
            self.body_hracu[index_hrace0] += (body_z_kola[0] + body_z_kola[1])//2
        else:
            self.body_hracu[index_hrace0] += body_z_kola[0]
            self.body_hracu[index_hrace1] += body_z_kola[1]

        self.vsechna_kola.append(kolo)

    def odehraj_turnaj(self):
        for i in range(len(self.vsichni_hraci)):
            for j in range(i, len(self.vsichni_hraci)):
                self.spust_kolo(200, i, j)


test_hrac0 = Hrac("Adam")
test_hrac1 = Hrac("Bára")

testovaci_turnaj = Turnaj([test_hrac0, test_hrac1])
testovaci_turnaj.odehraj_turnaj()

print(testovaci_turnaj.body_hracu)

