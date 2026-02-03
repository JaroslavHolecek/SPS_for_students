# Setter
# x, y, nazev nejsou ve skutečnosti atributy,
#             jsou to funkce @property (při čtení) a .setter (při zápisu)
#             které pracují se "speciálními" atributy _x, _y, _nazev
class Hrac:
  def __init__(self, hodnota_x, hodnota_y, nazev):
    self.x = hodnota_x # tady už se zavolá setter pro x
    self.y = hodnota_y
    self.nazev = nazev
  
  @property # co se má stát, pokud budeme číst x (název funkce)
  def x(self):
    return self._x

  @x.setter # co se má stát, pokud budem vkládat hodnotu do x (název funkce)
  def x(self, hodnota):
    self._x = max(hodnota, 0) # max(x,0) je fakticky stejné, jako: 0 if x < 0 else x

  @property
  def y(self):
    return self.__y

  @y.setter
  def y(self, hodnota):
    self.__y = max(hodnota, 0)

  @property
  def nazev(self):
    print("Čtu název hráče")
    return self._nazev

  @nazev.setter
  def nazev(self, hodnota):
    print("Zapisuji název hráče")
    self._nazev = hodnota

  def __str__(self):
    return "Hráč {} je na pozici x:{} y:{}".format(self.nazev, self.x, self.y)

H1 = Hrac(5, -15, "Žofka")
print(H1)
H1.x -= 25
print(H1)

print("======")
H1._x = -20 # jedno podtržítko je pouze nezávazné označení (upozornění, že bych zápis neměl dělat)
print(H1)