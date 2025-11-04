a = 21
b = 4
celociselne = a // b
zbytek = a % b
print("Integer:", a, "//", b, "=", celociselne, "zbytek", zbytek, type(celociselne) ,type(zbytek) )

a = 15.5
b = 3.1
celociselne = a // b
zbytek = a % b
print("Float:", a, "//", b, "=", celociselne, "zbytek", zbytek, type(celociselne) ,type(zbytek) )

#  index:      0      1        2       3     4    5    6
kamaradi = ["Adam", "Bára", "Cyril", 3.14, True, 10, ["A", "B"]]
print("List:", kamaradi, type(kamaradi))
print("Třetí kamarád je:", kamaradi[2])
print("Druhý odzadu je:", kamaradi[-2])
print("Některé:", kamaradi[1:6:2]) #od 1 do 5 s krokem 2

for kama in kamaradi:
    print("Kamarád:", kama*2)


napis = "Ahoj, jak se máš?"
print(napis)
for p in napis:
    print(p)

print(napis.upper())
print(napis.replace("j", "X"))
print(napis.replace(" ", ""))
print(napis.split(" "))