from enum import Enum

class MapElement(Enum):
    CIL = 0
    CESTA = 1
    PREKAZKA = 9

    def __str__(self):
        return self.name.lower()

def najdi_cile(mapa: list[list[int]]) -> list[tuple[int, int]]:
    souradnice_cilu = []
    for y, radek in enumerate(mapa):
        for x, prvek in enumerate(radek):
            if prvek == MapElement.CIL.value:
                souradnice_cilu.append((y, x))  # řádek, sloupec
    return souradnice_cilu

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
    print(mapa_vzdalenosti)

    cile = najdi_cile(map_grid)
    nastav_vzdalenost_cilu(mapa_vzdalenosti, cile)
    print(mapa_vzdalenosti)

    for cil in cile:
        sousedni_prujezdne = prujezdni_sousede(map_grid, cil)
        for soused in sousedni_prujezdne:
            okoli = sousede(rozmery, soused)
            minimum = nejmensi_hodnota(mapa_vzdalenosti, okoli)
            aktualni = mapa_vzdalenosti[soused[0]][soused[1]]
            mapa_vzdalenosti[soused[0]][soused[1]] = min(minimum+1, aktualni)

    print(mapa_vzdalenosti)






mapa = [[9,9,9,9],
        [1,1,1,0],
        [1,1,1,0],
        [9,9,9,9]]

compute_distance(mapa)

