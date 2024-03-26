from functools import cmp_to_key
import matplotlib.pyplot as plt
import random
import numpy as np


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

class HracJena(Hrac):

    def __init__(self):
        super().__init__("Jena")
        self.random_chance = 0.5

    def zahraj(self, tvuj_index, vysledky, body):
        if body[tvuj_index] < 50:
            return False
        elif body[tvuj_index] > 150:
            return True
        else:
            return random.random() < self.random_chance

class HracTit4TwoTats(Hrac):
    def __init__(self,):
        super().__init__("Tit4TwoTats")

    def zahraj(self, tvuj_index, vysledky, body):
        if len(vysledky) < 2:
            return True

        if not vysledky[-1][1-tvuj_index] and not vysledky[-2][1-tvuj_index]:
            return False # True/False

        return True

class HracT4t(Hrac):
    def __init__(self,):
        super().__init__("T4t")

    def zahraj(self, tvuj_index, vysledky, body):
        if tvuj_index+1 and vysledky == True:
            return True
        elif tvuj_index+1 and vysledky == False:
            return False

# Prvni tah vzdy True
# Pak mimikuje posledni tah protihrace s vyjimkou ze pokud vic jak 80% protihracovejch tahu je True/False tak zahraje toho misto toho
class THOXIV(Hrac):
    def __init__(self): super().__init__("THOXIV")

    def booltoint(self, b):
        if b == True: return 1
        else: return 0

    def zahraj(self, tvuj_index, vysledky, body):
        if vysledky == []: #prvni tah
            return True

        e_index = 1-tvuj_index
        vysledky_list = []
        karma = [0,0]
        for t in vysledky:
            for item in t:
                vysledky_list.append(item)
        for t in range(len(vysledky_list)):
            if t % 2 == 0:
                karma[0] += self.booltoint(vysledky_list[t])
            else:
                karma[1] += self.booltoint(vysledky_list[t])
        karma[0] = karma[0] / (len(vysledky_list) / 2)
        karma[1] = karma[1] / (len(vysledky_list) / 2)

        if vysledky_list[-2+tvuj_index] == True:
            if karma[e_index] < 0.2: return False
            else: return True
        else:
            if karma[e_index] > 0.8: return True
            else: return False

class Hrac_HODY_24(Hrac):
    def __init__(self,):
        super().__init__("Hody_24")

    def zahraj(self, tvuj_index, vysledky, body):
        if body[tvuj_index]> 10:
            return True
        else:
            return False

class HracBob(Hrac):
    def __init__(self,):
        super().__init__("HracBob")

    def zahraj(self, tvuj_index, vysledky, body):

        cislo = random.randint(1, 10)
        if tvuj_index % 2 == 5:
            if cislo > 5:
                return True
            else:
                return False
        else:
            if cislo < 5:
                return True
            else:
                return False

class HracMarek(Hrac):
    def __init__(self,sance):
        super().__init__("Marek")
        self.sance=sance

    def zahraj(self, tvuj_index, vysledky, body):
        if random.randint(0,100) <= self.sance:
            return False
        else:
            return True

class HracJozef(Hrac):
    def __init__(self):
        super().__init__("Jozef")

    def zahraj(self, tvuj_index, vysledky, body):
        if not vysledky : # prázdný seznam
            return True
        else:
            return vysledky[-1][1 - tvuj_index]

class HracPepa(Hrac):
    def __init__(self,):
        super().__init__("Pepa")

    def zahraj(self, tvuj_index, vysledky, body):
        if random.randint(0,1) == 1:
            return True # True/False
        else:
            return False

class HracLorenc(Hrac):
    def __init__(self,):
        super().__init__("Lorenc")

    def zahraj(self,tvuj_index, vysledky, body):
        if random.randint(0,1)==1:
            return True
        else:
            return False

class HracFerda(Hrac):
    def __init__(self,):
        super().__init__("Ferda")
    def zahraj(self, tvuj_index, vysledky, body):
        if (body[tvuj_index] % 2) == 0:
            return False
        else:
            return True

class HracIstvan(Hrac):
    def __init__(self,):
        super().__init__("Ištván")

    def zahraj(self, tvuj_index, vysledky, body):
        return False

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

    def odehraj_turnaj(self, pocet_opakovani):
        for i in range(pocet_opakovani):
            for prvni_i in range(len(self.vsichni_hraci)):
                for druhy_i in range(prvni_i, len(self.vsichni_hraci)):
                    self.odehraj_duel(self.pocet_kol_v_duelu, prvni_i, druhy_i )

    def ukaz_vysledky(self):
        for index, hrac in enumerate(self.vsichni_hraci):
            print(f"{hrac.jmeno:20} :\t{self.celkove_body_hracu[index]:6}")

    def zobraz_vysledky_graficky(self):
        # Seznam jmen hráčů
        jmena_hracu = [ hrac.jmeno for hrac in self.vsichni_hraci ]
        # Seznam dosažených skóre
        dosazene_skore = self.celkove_body_hracu

        # Unikátní indexy pro každého hráče
        unikatni_indexy = np.arange(len(jmena_hracu))

        # Vytvoření sloupcového grafu s duplicitními hodnotami
        plt.bar(unikatni_indexy, dosazene_skore, color='skyblue')

        # Nastavení popisků os
        plt.xlabel('Jména hráčů')
        plt.ylabel('Dosažené skóre')
        plt.title('Dosažené skóre hráčů')

        # Nastavení popisků x-ové osy
        plt.xticks(unikatni_indexy, jmena_hracu)

        # Zobrazení grafu
        plt.show()

ukazkovyTurnaj = Turnaj(
    [
        HracJarda(),
        HracTit4TwoTats(),
        HracTit4TwoTats(),
        HracTit4TwoTats(),
        HracTit4TwoTats(),
        HracTit4TwoTats(),
        HracJena(),
        HracT4t(),
        HracJozef(),
        THOXIV(),
        Hrac_HODY_24(),
        HracBob(),
        HracMarek(20),
        HracPepa(),
        HracLorenc(),
        HracFerda(),
        HracIstvan()
    ],
    200
)

ukazkovyTurnaj.odehraj_turnaj(5)

ukazkovyTurnaj.ukaz_vysledky()

ukazkovyTurnaj.zobraz_vysledky_graficky()





