limit = 15
vek = input("Zadej věk")
print(vek >= limit)

text = "Jen První Jsou Velká"
print(text)
print(text) # chceme všechna velká
print(text) # chceme najít pozici první mezery
print(text) # chceme všechna "o" nahradit "0", všechna "e" nahradit "3"

print(  100 * 3   + 30 ) # co bude výsledek
print(  30 + 100  * 3  )
print( (30 + 100) * 3  )

v = 10 == 10.0
print(v) # co bude výsledek

print(True and True)
print(False and False)
print(False and True)
print(True or True)
print(False or False)
print(False or True)
print(not True and True)
print(not False and False)
print(not False and True)

teplota = 10
if teplota < 0:
	print("Zima")
elif teplota < -20:
	print("Pořádná zima")
elif teplota > 30:
	print("Vedro")
else: 
	print("Nic speciálního")

print(1000 == 1_000)
print(10000000 == 1_000_000)

kamaradky = ["Alice", "Bára", "Cecílie", "Dáša", "Ema", "Fifinka"]
print(kamaradky[3:4])
print(kamaradky[3:])
print(kamaradky[2:-2])
print(kamaradky[:-1])
print(kamaradky[::-1])
print(kamaradky[::-2])

kamaradky += "Gabča"
print(kamaradky)

print("Gabča" in kamaradky)
print(kamaradky) # chci vědět, kolik mám kamarádek

for i in kamaradky:
	print(i)

# jak přiřadit kamarádkám pořadí?
for i in kamaradky:
	print(f"Ahoj {i}. kamaradko {i}")

print(range(800, 1000, 10)) # co se zobrazí?

# jaký je rozdíl mezi:
print( [10, 20, 30, 30] )
print( (10, 20, 30, 30) )
print( set([10, 20, 30, 30]) )







 