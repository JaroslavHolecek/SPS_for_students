from enum import Enum

class MapElement(Enum):
    CIL = 0
    CESTA = 1
    START = 2
    PREKAZKA = 9

    def __str__(self):
        return self.name.lower()

def nacti_mapu(file):
    mapa = []
    with open(file, "r") as f:
        for radek in f:
            mapa.append(
                [x for x in map(int, radek.split(" "))]
            )
    return mapa


def najdi_cile(mapa: list[list[int]]) -> list[tuple[int, int]]:
    souradnice_cilu = []
    for y, radek in enumerate(mapa):
        for x, prvek in enumerate(radek):
            if prvek == MapElement.CIL.value:
                souradnice_cilu.append((y, x))  # řádek, sloupec
    return souradnice_cilu

def najdi_start(mapa: list[list[int]]) -> tuple[int, int]:
    for y, radek in enumerate(mapa):
        for x, prvek in enumerate(radek):
            if prvek == MapElement.START.value:
                return (y, x)  # řádek, sloupec

def sousede(velikost: tuple[int, int], pozice: tuple[int, int]) -> list[tuple[int, int]]:
    vyska, sirka = velikost
    y, x = pozice
    mozni_sousede = [
        (y - 1, x),  # nahoru
        (y + 1, x),  # dolů
        (y, x - 1),  # vlevo
        (y, x + 1)   # vpravo
    ]
    # Vrátí jen ty sousedy, kteří jsou v rámci mapy
    return [
        (ny, nx) for ny, nx in mozni_sousede
        if 0 <= ny < vyska and 0 <= nx < sirka
    ]

def prujezdni_sousede(mapa: list[list[int]], pozice: tuple[int, int]) -> list[tuple[int, int]]:
    rozmery_mapy = (len(mapa), len(mapa[0]))
    sousedni_policka = sousede(rozmery_mapy, pozice)
    return [ (y,x) for y,x in sousedni_policka
             if mapa[y][x] != MapElement.PREKAZKA.value]

def vytvor_mapu_vzdalenosti(velikost: tuple[int, int]) -> list[list[int]]:
    vyska, sirka = velikost
    vychozi_hodnota = vyska * sirka
    return [[vychozi_hodnota for _ in range(sirka)] for _ in range(vyska)]

def nastav_vzdalenost_cilu(mapa_vzdalenosti, seznam_cilu):
    for y,x in seznam_cilu:
        mapa_vzdalenosti[y][x] = 0

def nejmensi_hodnota(mapa_vzdalenosti, seznam_policek):
    prvni_policko = seznam_policek[0]
    minimum = mapa_vzdalenosti[prvni_policko[0]][prvni_policko[1]]
    for policko in seznam_policek:
        hodnota = mapa_vzdalenosti[policko[0]][policko[1]]
        if hodnota < minimum:
            minimum = hodnota

    return minimum


def compute_distance(map_grid):
    rozmery = (len(map_grid), len(map_grid[0]))
    mapa_vzdalenosti = vytvor_mapu_vzdalenosti(rozmery)

    cile = najdi_cile(map_grid)
    nastav_vzdalenost_cilu(mapa_vzdalenosti, cile)

    zapsane = set(cile)
    aktualni = set()
    for cil in cile:
        okoli = set(prujezdni_sousede(map_grid, cil))
        aktualni.update(okoli)

    while len(aktualni) > 0:
        k_zapsani = set()
        for akt in aktualni:
            # nastaveni hodnot pro aktualni
            okoli = sousede(rozmery, akt)
            minimum = nejmensi_hodnota(mapa_vzdalenosti, okoli)
            hodnota_akt = mapa_vzdalenosti[akt[0]][akt[1]]
            mapa_vzdalenosti[akt[0]][akt[1]] = min(minimum + 1, hodnota_akt)

            sousedi = set(prujezdni_sousede(map_grid, akt))
            k_zapsani.update((sousedi - zapsane) - aktualni)

        zapsane.update(aktualni)
        aktualni = k_zapsani.copy()

    return mapa_vzdalenosti

def show_2d(array2d):
    for radek in array2d:
        print("\t".join(map(str,radek)))

def vzdalenosti_od_okraju_a_prekazek(mapa: list[list[int]]) -> list[list[dict]]:
    vyska = len(mapa)
    sirka = len(mapa[0])
    vysledky = [[{'up': 0, 'down': 0, 'left': 0, 'right': 0} for _ in range(sirka)] for _ in range(vyska)]

    for y in range(vyska):
        for x in range(sirka):
            if mapa[y][x] == MapElement.PREKAZKA.value:
                continue  # Překážka sama nemá smysl měřit

            # Nahoru
            vzd = 0
            for ny in range(y - 1, -1, -1):
                if mapa[ny][x] == MapElement.PREKAZKA.value:
                    break
                vzd += 1
            vysledky[y][x]['up'] = vzd

            # Dolů
            vzd = 0
            for ny in range(y + 1, vyska):
                if mapa[ny][x] == MapElement.PREKAZKA.value:
                    break
                vzd += 1
            vysledky[y][x]['down'] = vzd

            # Vlevo
            vzd = 0
            for nx in range(x - 1, -1, -1):
                if mapa[y][nx] == MapElement.PREKAZKA.value:
                    break
                vzd += 1
            vysledky[y][x]['left'] = vzd

            # Vpravo
            vzd = 0
            for nx in range(x + 1, sirka):
                if mapa[y][nx] == MapElement.PREKAZKA.value:
                    break
                vzd += 1
            vysledky[y][x]['right'] = vzd

    return vysledky




if __name__ == "__main__":
    mapa = nacti_mapu("mapy/mapa2.txt")

    mapa_vzdalenosti = compute_distance(mapa)

    show_2d(mapa)
    print()
    show_2d(mapa_vzdalenosti)

    vzdalenost_prekazek = vzdalenosti_od_okraju_a_prekazek(mapa)
    show_2d(vzdalenost_prekazek)
