import os
print(os.getcwd())

# Zápis do souboru
with open('ukazkovy.txt', 'w', encoding='utf-8') as soubor:
  soubor.write('Toto je ukázkový text.\n')
  soubor.write('Další řádek textu.\n')

# Čtení ze souboru
with open('ukazkovy.txt', 'r', encoding='utf-8') as s:
  obsah = s.readline()
  print(obsah)

with open('ukazkovy.txt', 'r', encoding='utf-8') as s:
  for radek in s:
    print("Řádek v souboru:", radek)