import random

seznam = [

]

while True:
    vstup = input()
    if vstup == "l":
        print(random.choice(seznam))
    elif vstup == "k":
        break