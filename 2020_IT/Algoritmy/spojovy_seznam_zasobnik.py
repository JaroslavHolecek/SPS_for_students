class Prvek:
    def __init__(self, zprava:str, dalsi=None):
        self.zprava = zprava
        self.dalsi = dalsi
        
class Zasobnik:
    def __init__(self, kapacita):
        self.kapacita = kapacita
        self.velikost = 0
        self.prvni:Prvek = None
        
    def precti(self):
        print("======")
        aktualni = self.prvni
        if self.velikost == 0:
            print("Zásobník je prázdný")
        while aktualni is not None:
            print(aktualni.zprava)
            aktualni = aktualni.dalsi
        
    def pridej_prvek(self, pridan:Prvek):
        if self.kapacita > self.velikost:
            pridan.dalsi = self.prvni
            self.prvni = pridan
            self.velikost += 1
        else:
            print("Plná kapacita, prvek nepřidán.")
    def smaz_prvek(self):
        aktualni = self.prvni
        if self.velikost == 1:
            self.prvni = None
            self.velikost -= 1
        elif self.velikost == 0:
            print("Pokoušíš se mazat z prázdného Zásobníku")
        else:
            self.prvni = self.prvni.dalsi
            self.velikost -= 1
    
f = Zasobnik(3)
f.pridej_prvek(Prvek("Ahoj"))
f.pridej_prvek(Prvek("Nazdar"))
f.pridej_prvek(Prvek("Čus"))
f.precti()
f.pridej_prvek(Prvek("Navíc"))
f.precti()
f.smaz_prvek()
f.precti()
f.smaz_prvek()
f.smaz_prvek()
f.precti()
f.smaz_prvek()