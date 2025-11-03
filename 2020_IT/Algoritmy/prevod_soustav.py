from typing import List

cislo_na_text = {
        0 : "0",
        1 : "1",
        2 : "2",
        3 : "3",
        4 : "4",
        5 : "5",
        6 : "6",
        7 : "7",
        8 : "8",
        9 : "9",
        10 : "a",
        11 : "b",
        12 : "c",
        13 : "d",
        14 : "e",
        15 : "f"
}

class Cislo:
    def __init__(self, hodnoty:List[int], soustava:int):
        self.hodnoty = hodnoty
        self.soustava = soustava
    
    def hodnotaVDesitkove(self):
        vysledek = 0
        for index, hodnota in enumerate(reversed(self.hodnoty)):
            vysledek += hodnota * (self.soustava ** index)
        return vysledek
    
    def prevodDoLibovolne(self, cilovaSoustava):
        hodnota = self.hodnotaVDesitkove()
        cilovaHodnota: List[int] = []
        while hodnota > 0:
            cilovaHodnota.append(hodnota % cilovaSoustava) # zbytky jsou hodnoty cifer v cílovem čísle
            hodnota = hodnota // cilovaSoustava
        
        return Cislo(list(reversed(cilovaHodnota)), cilovaSoustava) # zbytky jsou sepsané v opačném pořadí
  
    def __str__(self):
        return f"{self.soustava}: {''.join([cislo_na_text.get(cislo,'N') for cislo in self.hodnoty])}"
        
c1 = Cislo([1,1,1,1,0,1,0,0,1,1], 2)
c2 = c1.prevodDoLibovolne(10)
print(c1, c2)
print(c1.hodnotaVDesitkove(), c2.hodnotaVDesitkove())
c3 = c2.prevodDoLibovolne(32)
print(c3)