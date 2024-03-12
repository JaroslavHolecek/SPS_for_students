class Hrac():
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def zahraj(self, tvuj_index, vysledky, body):
        return True

# Tuto třídu dopište vy - minimálně obsah funkce zahraj
class HracJarda(Hrac):
    def __init__(self,):
        super().__init__("Jarda")

    def zahraj(self, tvuj_index, vysledky, body):
        return True # True/False


class Duel:
    def __init__(self, pocet_kol, hrac0, hrac1):
        self.cislo_kola = 0
        self.pocet_kol = pocet_kol
        self.hrac0 = hrac0
        self.hrac1 = hrac1
        self.vysledky = [] # [ (T,F), (F,F), (T,T), ... ]
        self.body = [0, 0]

    def odehraj_duel(self):
        while self.cislo_kola < self.pocet_kol:
            self.zahraj_kolo()

        return self.body

    def zahraj_kolo(self):
        self.cislo_kola += 1
        tah0 = self.hrac0.zahraj(0, self.vysledky, self.body)
        tah1 = self.hrac1.zahraj(1, self.vysledky, self.body)
        self.vysledky.append((tah0, tah1))

        if tah0 and tah1: # oba spolupracovali
            self.body[0] += 3
            self.body[1] += 3
        elif tah0 and not tah1:
            self.body[0] += 0
            self.body[1] += 5
        elif not tah0 and tah1:
            self.body[0] += 5
            self.body[1] += 0
        else:
            self.body[0] += 1
            self.body[1] += 1


class Turnaj:
    def __init__(self, vsichni_hraci, pocet_kol_v_duelu):
        self.vsichni_hraci = vsichni_hraci
        self.celkove_body_hracu = [0] * len(vsichni_hraci)
        self.vsechny_duely = []
        self.pocet_kol_v_duelu = pocet_kol_v_duelu

    def odehraj_duel(self, pocet_kol, hrac0_index, hrac1_index):
        duel = Duel(pocet_kol,
                    self.vsichni_hraci[hrac0_index],
                    self.vsichni_hraci[hrac1_index])
        body = duel.odehraj_duel()

        self.vsechny_duely.append(duel)
        self.celkove_body_hracu[hrac0_index] += body[0]
        self.celkove_body_hracu[hrac1_index] += body[1]

    def odehraj_turnaj(self):
        for prvni_i in range(len(self.vsichni_hraci)):
            for druhy_i in range(prvni_i, len(self.vsichni_hraci)):
                self.odehraj_duel(self.pocet_kol_v_duelu, prvni_i, druhy_i )


ukazkovyTurnaj = Turnaj(
    [
        Hrac("Adam"),
        Hrac("Bára"),
        Hrac("Cyril"),
        Hrac("Dáša")
    ],
    200
)

ukazkovyTurnaj.odehraj_turnaj()

print(ukazkovyTurnaj.celkove_body_hracu)





