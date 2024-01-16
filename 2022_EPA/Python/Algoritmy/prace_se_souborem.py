import linearni_kvadraticka_rce as rce


with open("muj_prvni_soubor.txt", "r") as soubor:
    # obsah_souboru = soubor.read()
    for radek in soubor:
        print("Radek souboru je:", radek) # "7 8 9"
        rozdelene = radek.split() #["7", "8", "9"]
        a, b, c = map(int, rozdelene)
        rce.kvadraticka_rovnice(a, b, c) # 7,8,9

with open("muj_prvni_soubor.txt", "r") as soubor:
    for radek in soubor:
        a, b, c = map(int, radek.split())
        rce.kvadraticka_rovnice(a, b, c) # 7,8,9



# print(obsah_souboru)