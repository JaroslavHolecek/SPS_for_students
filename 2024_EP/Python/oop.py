# vytvořením třídy jsme NEvytvořili žádný objekt
class Auto: # třída ("šablona") pro objekty Auto
  def __init__ (self, x, y, nazev): # tato metoda se spustí při vytváření objektu
    self.pozice = [x,y]
    self.hp = 0
    self.nazev = nazev

  def __str__(self): # speciální metoda __str__() určuje, jak se objekt převede na string
    return "Auto {} s hp {} na pozici {}".format(self.nazev, self.hp, self.pozice)
  
  def popojed_vpravo(self):
    self.pozice[0] += 10

auto1 = Auto(0,0,"Škodovka") # zde vytváříme objekt typu Auto - tedy spouštíme metodu __init__() ve třídě Auto
auto2 = Auto(10,20,"Trabant")
auto3 = Auto(300,400,"Ferrari")

print(auto1)

for _ in range(10):
  auto1.popojed_vpravo()

print(auto1)

while auto1.pozice[0] < 300:
  auto1.popojed_vpravo()
  print(auto1)

print(auto2)
