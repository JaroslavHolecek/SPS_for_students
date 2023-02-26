def zasifruj_caesar(zprava, klic):
    zasifrovana_zprava=""
    for pismenko in zprava:
        if pismenko.isalpha():
            if pismenko.isupper():
                ASCII_posun = 65
            else:
                ASCII_posun = 97
            zasifrovana_zprava += chr((ord(pismenko) - ASCII_posun + klic) % 26 + ASCII_posun)
        else:
            zasifrovana_zprava += " "
        # index_z_pismenka = ord(pismenko) - 97
        # zasifrovany_index = (index_z_pismenka + klic) % 26
        # pismenko_z_indexu = chr(zasifrovany_index + 97)
        # zasifrovana_zprava += pismenko_z_indexu
    return zasifrovana_zprava

def desifruj_caesar(zprava, klic):
    return zasifruj_caesar(zprava, -klic)


def zasifruj_caesar_oneline(zprava, klic):
    return "".join([chr((ord(pismenko) - 97 + klic) % 26 + 97) for pismenko in zprava])
    
    # i s kontrolami uz kód není úplně přehledný...
    # return "".join([chr((ord(pismenko) - (65 if pismenko.isupper() else 97) + klic) % 26 + (
    #     65 if pismenko.isupper() else 97)) if pismenko.isalpha() else " " for pismenko in zprava])

def desifruj_caesar_oneline(zprava, klic):
    return zasifruj_caesar_oneline(zprava, -klic)

zprava = "Ahoj jak se mas prave jsem na obede"
klic = 3
sifra = zasifruj_caesar(zprava, klic)
desifrovana = desifruj_caesar(sifra, klic)
print(f"Zpráva {zprava}\nzašifrovaná: {sifra}\ndesifrovaná: {desifrovana}")

zprava = "nejkulatoulinkatejsi"
sifra = zasifruj_caesar_oneline(zprava, klic)
desifrovana = desifruj_caesar_oneline(sifra, klic)
print(f"Zpráva {zprava}\nzašifrovaná: {sifra}\ndesifrovaná: {desifrovana}")
