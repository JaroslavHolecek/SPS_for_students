# TODO: zde vytvořte třídu
class Zeton:
  def __init__(self, x,y, h):
    self.pozice = [x,y]
    self.hodnota = h

# Dále už kód neměňte
vsechny_zetony = []
for i in range(0,5):
  vsechny_zetony.append(Zeton(-i, 10*i, 7*i))

print("Existuje {} Žetonů:".format(len(vsechny_zetony)))
for i, z in enumerate(vsechny_zetony):
  print("{}. pozice: {} hodnota {}".format(i+1, z.pozice, z.hodnota))