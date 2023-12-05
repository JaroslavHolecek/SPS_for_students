import random

seznam = ["Bohuněk Jan", "Čermáková Aneta",
"Dundr Vojtěch",
"Giedrys Robertas",
"Hodač David",
"Hofman Tomáš",
"Hrdý Stanislav",
"Hubička Jan",
"Kovařík Michal",
"Lorenc Petr",
"Maňásek Daniel",
"Matura Dominik",
"Nedvídek Mikoláš Artur"]

while len(seznam) > 0:
    input()
    vybrany = random.choice(seznam)
    print(vybrany)
    seznam.remove(vybrany)
