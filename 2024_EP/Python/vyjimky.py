# NEPŘEHLEDNÁ VERZE
# cislo1 = int(input("Zapiš dělenec: "))

# vstup = input("Zapiš dělitel: ")
# if not vstup.isnumeric():
#     print("Chyba: Dělitel musí být číslo.")

# cislo2 = int(vstup)
# if cislo2 == 0:
#     print("Dělitel je nula, nelze dělit.")

# vysledek = cislo1 / cislo2
# print("Podíl:", vysledek)

# PŘEHLEDNÁ VERZE S VYJÍMKAMI
try:
  cislo1 = int(input("Zapiš dělenec: "))
  cislo2 = int(input("Zapiš dělitel: "))
  vysledek = cislo1 / cislo2
  print("Podíl:", vysledek)
except ValueError:
  print("Chyba: vstup musí být číslo!")
except ZeroDivisionError:
  print("Chyba: Nelze dělit nulou!")
except Exception as e:
  print("Nastala neočekávaná chyba:", e)