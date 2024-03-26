import numpy as np
import random
import matplotlib.pyplot as plt

class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def zahraj(self, muj_index, minule_tahy, score):
        return False # Podvádí v každém kole

class HracJarda(Hrac):
    def __init__(self):
        super().__init__("Jarda")
        # zde si muzete vytvorit jakekoliv vlastni promenne

    def zahraj(self, muj_index, minule_tahy, score):
        # Tuto funkci vyplnit vlastní strategií
        return False

class HracNeo(Hrac):
    def __init__(self):
        super().__init__("Neo")
        # zde si muzete vytvorit jakekoliv vlastni promenne

    def zahraj(self, muj_index, minule_tahy, score):
        # Tuto funkci vyplnit vlastní strategií
        moje_score = score[muj_index]
        if moje_score % 2 == 0:
            return False
        else:
            return True

class HracBobo(Hrac):
    def __init__(self):
        super().__init__("BoBo")
        # zde si muzete vytvorit jakekoliv vlastni promenne

    def zahraj(self, muj_index, minule_tahy, score):
        # Hrac strida spolupraci nebo nespolupracuje
        if len(minule_tahy)%2==0:
            return True
        else:
            return False

class HracLukas(Hrac):
    def __init__(self):
        super().__init__("Lukas")
        self.pocet = 0
        self.tah = True
        # vytvořil jsem si hráče Lukase

    def zahraj(self, muj_index, minule_tahy, score):
        # dvakrát spolupracuje a dvakrát podvádí
        self.pocet += 1
        if self.pocet >= 2:
             self.tah = not self.tah
             self.pocet = 0
        return self.tah

class HracNahoda(Hrac):
    def __init__(self):
        super().__init__("Pan Vojtíšek")
        # zde si muzete vytvorit jakekoliv vlastni promenne

    def zahraj(self, muj_index, minule_tahy, score):
        # Je potreba importovat random - from random import random.
        # Hrac vybira nahodne, zda-li bude spolupracovat, ci nikoliv.
        nahodnaHodnota = random.random()
        if nahodnaHodnota >= 0.5:
            return True
        else:
            return False

class HracMartin(Hrac):
    def __init__(self):
        super().__init__("Martin")
        self.counter = 0  # Počítadlo tahů

    def zahraj(self, muj_index, minule_tahy, score):
        self.counter += 1  # Inkrementace počítadla tahů
        if self.counter % 15 == 0:  # Každý desátý tah
            return True
        if minule_tahy:
            posledni_tah_soupera = minule_tahy[-1][1-muj_index]  # Poslední tah soupeře
            if posledni_tah_soupera:  # Pokud soupeř zahrál kladný tah
                return True  # Hrát kladný tah
            else:  # Pokud soupeř zahrál záporný tah
                return False  # Záporný tah
        else:
            return True  # Pokud je to první tah, vracíme vždy True (kladný tah)

class HracBageta(Hrac):
    def __init__(self):
        super().__init__("Bageta")
        self.opponent_moves = []

    def zahraj(self, muj_index, minule_tahy, score):
        if len(minule_tahy) == 0:
            return bool(random.getrandbits(1))  # Random první kolo
        else:
            opponent_last_move = minule_tahy[-1][1 - muj_index]
            self.opponent_moves.append(opponent_last_move)
            if self.detect_spamming_false():
                return False  # False spam když protivník spamuje False
            elif len(minule_tahy) >= 2 and minule_tahy[-1][1 - muj_index] == minule_tahy[-2][1 - muj_index]:
                return not minule_tahy[-1][1 - muj_index]  # Změna stragtegie na counter protivníka
            else:
                return minule_tahy[-1][1 - muj_index]  # Opakovat protivníkův tah

    def detect_spamming_false(self):
        # False spam check
        if len(self.opponent_moves) >= 4:
            return all(move == False for move in self.opponent_moves[-4:])
        else:
            return False

class HracHonzyk(Hrac):
    def __init__(self):
        super().__init__("Honzyk")

    def zahraj(self, muj_index, minule_tahy, score):
        kolo = len(minule_tahy) + 1
        index_protihrace = 1 - muj_index
        if kolo <= 3:
            return True # v prvnich trech kolech bude spolupracovat
        elif kolo > 3 and kolo < 200:
            posledni_tri_tahy_protihrace = [
                minule_tahy[len(minule_tahy) - 1][index_protihrace],
                minule_tahy[len(minule_tahy) - 2][index_protihrace],
                minule_tahy[len(minule_tahy) - 3][index_protihrace]
            ] # ulozi si posledni tri tahy protihrace

            vysledek = max(set(posledni_tri_tahy_protihrace), key = posledni_tri_tahy_protihrace.count) # z poslednich tri tahu protihrace si vezme nejcasteji se vyskytujici

            return vysledek
        else:
            return False # v poslednim kole bude podvadet

class Duel:
    def __init__(self, hrac0:Hrac, hrac1:Hrac, delka_duelu):
        self.hrac0 = hrac0
        self.hrac1 = hrac1
        self.delka_duelu = delka_duelu

        self.score = [0, 0]
        self.vyvoj_score = [(0,0)]
        self.minule_tahy = [] # [(T,T), (T,F), ...]

    def odehraj_tah(self):
        tah0 = self.hrac0.zahraj(0, self.minule_tahy.copy(), self.score.copy())
        tah1 = self.hrac1.zahraj(1, self.minule_tahy.copy(), self.score.copy())

        self.minule_tahy.append( (tah0, tah1) )
        if tah0 and tah1:
            self.score[0] += 3
            self.score[1] += 3
        elif not tah0 and not tah1:
            self.score[0] += 1
            self.score[1] += 1
        elif tah0 and not tah1:
            self.score[0] += 0
            self.score[1] += 5
        else:
            self.score[0] += 5
            self.score[1] += 0

        self.vyvoj_score.append((self.score.copy()))

    def odehraj_duel(self):
        for i in range(self.delka_duelu):
            self.odehraj_tah()

        # Extrahovat x a y hodnoty pro obě datové sady
        x = range(len(self.vyvoj_score))
        y1 = [x for (x,y) in self.vyvoj_score]
        y2 = [y for (x,y) in self.vyvoj_score]

        # Vytvořit spojnicový graf pro obě datové sady
        plt.plot(x, y1, marker='o', linestyle='-', label='Datová sada 1')
        plt.plot(x, y2, marker='o', linestyle='-', label='Datová sada 2')

        # Přidat popisky os a titulek
        plt.xlabel('Index')
        plt.ylabel('Hodnota')
        plt.title('Vývoj hodnoty v čase')

        # Přidat legendu
        plt.legend()

        # Zobrazit graf
        plt.grid(True)  # Přidat mřížku
        plt.show()

class Turnaj:
    def __init__(self, seznam_hracu, delka_duelu):
        self.seznam_hracu = seznam_hracu
        self.body = [0] * len(self.seznam_hracu)
        self.seznam_duelu = []
        self.delka_duelu = delka_duelu

    def odehraj_turnaj(self):
        for i0, prvni in enumerate(self.seznam_hracu):
            for i1, druhy in enumerate(self.seznam_hracu[i0:], i0):
                duel = Duel(prvni, druhy, self.delka_duelu)

                duel.odehraj_duel()

                if i0 == i1:
                    self.body[i0] += (duel.score[0] + duel.score[1])//2
                else:
                    self.body[i0] += duel.score[0]
                    self.body[i1] += duel.score[1]

    def ukaz_vysledky(self):
        for index, hrac in enumerate(self.seznam_hracu):
            print(f"{hrac.jmeno:20} :\t{self.body[index]:6}")

    def zobraz_body_grafricky(self):
        # Příklad dat: jména hráčů a dosažené skóre
        jmena_hracu = [hrac.jmeno for hrac in self.seznam_hracu]
        dosazene_skore = self.body

        # Vytvoření sloupcového grafu
        plt.bar(jmena_hracu, dosazene_skore, color='skyblue')

        # Přidání popisků
        plt.xlabel('Jméno hráče')
        plt.ylabel('Skóre')
        plt.title('Dosažené skóre hráčů')

        # Zobrazení grafu
        plt.show()

testovaciTurnaj = Turnaj(
    [
        HracJarda(),
        HracNeo(),
        HracBobo(),
        HracLukas(),
        HracNahoda(),
        HracMartin(),
        HracBageta(),
        HracHonzyk()
    ],
    200)

testovaciTurnaj.odehraj_turnaj()

testovaciTurnaj.ukaz_vysledky()

testovaciTurnaj.zobraz_body_grafricky()



