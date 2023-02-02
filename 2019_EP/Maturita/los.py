import random

seznam = [
"Baroch Matěj",
"Šístek Roman",
"Veselý Vojtěch",
"Zámiš David",
]

while True:
    vstup = input()
    if vstup == "l":
        print(random.choice(seznam))
    elif vstup == "k":
        break