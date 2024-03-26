def Eratosthenovo_sito(N):
    # Seznam 1-N
    seznam = list(range(1, N+1))
    # pro čísla od dvou do odmocniny z N
    for cislo in range(2, int(N**(1/2))+1):
        # pro čísla, která nejsou v seznamu
        if cislo in seznam:
    #   vyškrtat všechny násobky čísla ze seznamu
            for nasobek in range(2*cislo, N+1, cislo):
                if nasobek in seznam:
                    seznam.remove(nasobek)
    #   Výsledek je v seznamu
    return seznam

try:
    soubor_vstup = "vstupy.txt"
    soubor_vystup = "vysledky.txt"

    with open(soubor_vstup, 'r') as f_in, open(soubor_vystup, 'w') as f_out:
        for line in f_in:
            try:
                maximalni_cislo = int(line.strip())
                prvoctisla = Eratosthenovo_sito(maximalni_cislo)
                f_out.write(f"Prvočísla pro {maximalni_cislo}: {prvoctisla}\n")
            except ValueError:
                f_out.write("Neplatný vstup v souboru. Ignoruji řádek.\n")
except FileNotFoundError:
    print("Soubor nenalezen.")
except PermissionError:
    print("Nemáte oprávnění ke čtení/zápisu souboru.")
except IOError:
    print("Nastala chyba při čtení/zápisu souboru.")
except Exception:
    print("Neočekávaná chyba - kontaktujte vývojáře na: email")



