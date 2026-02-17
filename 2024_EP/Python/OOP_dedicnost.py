class Zvire:
  # Každé zvíře má své jméno a hmotnost
  def __init__(self, jmeno, hmotnost):
    if hmotnost < 0:
      raise ValueError("Hmotnost Zvířete nemůže být záporná")
    self.jmeno = jmeno
    self.hmotnost = hmotnost    

  @property
  def jmeno(self):
    return self.__jmeno
  @jmeno.setter
  def jmeno(self, jmeno):
    self.__jmeno = jmeno.upper()

  @property
  def hmotnost(self):
    return self.__hmotnost
  @hmotnost.setter
  def hmotnost(self, hmotnost):
    self.__hmotnost = max(0, hmotnost)

  # Každé zvíře umí zařvat
  def zarvi(self):
    print("Huááá hlasitostí") 

  def __str__(self):
    return "Volej na mě {} a vážím {}*tíhové_zrychlení".format(self.jmeno, self.hmotnost)
  
class Pes(Zvire):
  # Při "výrobě" Psa nejprve vyrobíme zvíře a potom doplníme vlastnosti navíc
  def __init__(self, jmeno, hmotnost, hlasitost):
    Zvire.__init__(self, jmeno, hmotnost)
    self.hlasitost = hlasitost

  # Pes řve jinka než obyčejné zvíře
  def zarvi(self):
    print(f"Haf haf hlasitostí {self.hlasitost}") 

  # Zobrazení Psa je kombinace Zvířete a speciálních vlastností 
  def __str__(self):
    return "Jsem pes hlasitý {} {}".format(self.hlasitost, Zvire.__str__(self))

class Kocka(Zvire):
  def __init__(self, jmeno, hmotnost, roztomilost):
    Zvire.__init__(self, jmeno, hmotnost)
    self.roztomilost = roztomilost

  def zarvi(self):
    print(f"Mňau mňau s roztomilostí {self.roztomilost}") 

  def __str__(self):
    return "Jsem kočka na {} roztomilá {}".format(self.roztomilost, Zvire.__str__(self))

p1 = Pes("Bára", 40, 90)
k1 = Kocka("Cecilka", 3, 100)

print(p1)
p1.zarvi()
print(k1)
k1.zarvi()

z1 = Zvire("Anička", 30)
print(z1)
z1.zarvi()



# veterinarni osetreni můžeme provést na každém zvířeti
def veterinarni_osetreni(zvire:Zvire):
  print("Osetruji {} ...".format(zvire))
  zvire.zarvi() # pri osetreni
  print("Hotovo.")



veterinarni_osetreni(z1)
veterinarni_osetreni(p1)
veterinarni_osetreni(k1)
     

     
