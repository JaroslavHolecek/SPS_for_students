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

class Duel:
    def __init__(self, hrac0:Hrac, hrac1:Hrac, delka_duelu):
        self.hrac0 = hrac0
        self.hrac1 = hrac1
        self.delka_duelu = delka_duelu

        self.score = [0, 0]
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

    def odehraj_duel(self):
        for i in range(self.delka_duelu):
            self.odehraj_tah()


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


testovaciTurnaj = Turnaj(
    [
        HracJarda(),
        Hrac("Bára"),
        Hrac("Cyril"),
        Hrac("Dan")
    ],
    200)

testovaciTurnaj.odehraj_turnaj()

print(testovaciTurnaj.body)



