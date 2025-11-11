class obdelnik():
    def __init__(self,zadana_sirka,zadana_delka,zadana_barva):
        self.setSirka(zadana_sirka)
        self.delka = zadana_delka
        self.barva = zadana_barva
    
    def setSirka(self,s):
        if s < 0:
            s=s*-1
        self._sirka = s
        
    def getSirka(self):
        return self._sirka
        
    def __str__(self):
        #return str(self.sirka)+" "+str(self.delka)+" "+self.barva
        return f"{self._sirka} {self.delka} {self.barva}"
        #return "{} {} {}".format(self.sirka, self.delka, self.barva)
    
    def obsah(self):
        return self._sirka * self.delka
    
    def obvod(self):
        return 2 * self._sirka + 2 * self.delka

    def zvetsit(self,x,y):
        self._sirka=self._sirka+x
        self.delka+=y
        
class ctverec(obdelnik):
    def __init__(self, zadana_sirka, zadana_barva):
        obdelnik.__init__(self, zadana_sirka, zadana_sirka, zadana_barva)

    def __str__(self):
        return f"{self._sirka} {self.barva}"
    
    def zvetsit(self, x):
        obdelnik.zvetsit(self, x, x)
    
obdelnik2 = obdelnik(-30, 80, "blue")
print(obdelnik2, obdelnik2.obvod(), obdelnik2.obsah())
obdelnik2.zvetsit(20, 30)
print(obdelnik2, obdelnik2.obvod(), obdelnik2.obsah())

ctverec1 = ctverec(100, "orange")
print(ctverec1, ctverec1.obvod(), ctverec1.obsah())
ctverec1.zvetsit(10)
print(ctverec1, ctverec1.obvod(), ctverec1.obsah())

