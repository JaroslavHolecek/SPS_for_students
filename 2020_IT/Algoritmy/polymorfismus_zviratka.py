class Zvire():
    def __init__(self, jmeno):
        self.jmeno=jmeno
    
    def vydejZvuk(self):
        print("brum")
        
class Pes(Zvire):
    def vydejZvuk(self):
        print("haf")
    
    def na_prochazku(self, barva_voditka, misto):
        print("Jdu na", misto, "a mam", barva_voditka, "voditko")
        
class Kocka(Zvire):
    def vydejZvuk(self):
        print("mnau")
        
    def na_prochazku(self):
        print("Kočky jsou na procházce pořád")
        
class Zelva(Zvire):
    def vydejZvuk(self):
        print("vzum")
        
    def na_prochazku(self, kam):
        print("Teď jsem se z", kam, "vrátila")

class Veterinar:
    def __init__(self, cena):
        self.cena=cena
        
    def vysetri(self, Z:Zvire):
        Z.vydejZvuk()
        
v1=Veterinar(100)
p1=Pes("alik")
k1=Kocka("alex")
z1=Zelva("pepa")
v1.vysetri(p1)
v1.vysetri(k1)
v1.vysetri(z1)

p1.na_prochazku("modré","do lesa")
k1.na_prochazku()
z1.na_prochazku("z pláže")

def secti(*args):
    vysledek = 0
    for a in args:
        vysledek += a
    return vysledek

max = "Ahoj"

print(secti(1,2,4))




