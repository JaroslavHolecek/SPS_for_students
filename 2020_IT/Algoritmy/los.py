import random
seznam = ["Antoň Filip", "Antoň Lukáš", "Bartl Filip", "Fikart Tomáš",
          "Filipp Martin", "Funda Filip", "Kindl Tomáš", "Mašek Alex",
          "Mišovic Matěj", "Poslední Martin", "Prokop David", "Smetana Tomáš",
          "Zenáhlík Pavel", "Žák Martin"]

while seznam:
    vybrany = random.choice(seznam)
    print(vybrany)
    seznam.remove(vybrany)
    input()

