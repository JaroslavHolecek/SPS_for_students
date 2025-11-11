import pygame
import mysql.connector
pygame.init()

class Stav_hry():
    def __init__(self):
        """
        Pole šachů je značeno 2D listem
        30 značí prázdné políčko
        1x značí černou barvu
        2x značí bílou barvu
        x1 značí krále (king)
        x2 značí dámu (queen)
        x3 značí věž (rook)
        x4 značí střelce (bishop)
        x5 značí jezdce (knight)
        x6 značí pěšce (pawn)
        """
        self.pole = [
            ["13", "15", "14", "12", "11", "14", "15", "13"],
            ["16", "16", "16", "16", "16", '16', "16", "16"],
            ["30", "30", "30", "30", "30", "30", "30", "30"],
            ["30", "30", "30", "30", "30", "30", "30", "30"],
            ["30", "30", "30", "30", "30", "30", "30", "30"],
            ["30", "30", "30", "30", "30", "30", "30", "30"],
            ["26", "26", "26", "26", "26", "26", "26", "26"],
            ["23", "25", "24", "22", "21", "24", "25", "23"]
        ]
        self.bily_na_tahu = True # Určuje, kdo je na tahu (True = bílý, False = černý)
        self.zaznam_pohybu = []

    def udelej_pohyb(self, pohyb):
        if self.pole[pohyb.pocatecni_radek][pohyb.pocatecni_sloupec] != "30":  # Kontroluje, jestli je počáteční čtverec prázdný
            self.pole[pohyb.pocatecni_radek][pohyb.pocatecni_sloupec] = "30" # Počáteční čtverec figurky se vyprázdní
            self.pole[pohyb.koncovy_radek][pohyb.koncovy_sloupec] = pohyb.hybnuta_figurka
            self.zaznam_pohybu.append(pohyb) # Zaznamená pohyb, abychom ho později mohli později vrátit
            self.bily_na_tahu = not self.bily_na_tahu # Prohodí hráče

    def vratit_tah(self):
        if len(self.zaznam_pohybu) != 0: # Ujišťuje, zda byl už proveden aspoň 1 tah
            tah = self.zaznam_pohybu.pop()
            self.pole[tah.pocatecni_radek][tah.pocatecni_sloupec] = tah.hybnuta_figurka
            self.pole[tah.koncovy_radek][tah.koncovy_sloupec] = tah.sebrana_figurka
            self.bily_na_tahu = not self.bily_na_tahu # Prohodí tah

class Pohyb():
    # Přiřadí klíče k hodnotám
    horizontala_do_radku = {"1": 7, "2": 6, "3": 5, "4": 4,
                            "5": 3, "6": 2, "7": 1, "8": 0}
    horizontala_do_radku = {hodnota: klic for klic, hodnota in horizontala_do_radku.items()}
    vertikala_do_sloupce = {"a": 0, "b": 1, "c": 2, "d": 3,
                          "e": 4, "f": 5, "g": 6, "h": 7}
    vertikala_do_sloupce = {hodnota: klic for klic, hodnota in vertikala_do_sloupce.items()}

    def __init__(self, pocatecni_ctverec, koncovy_ctverec, pole):
        self.pocatecni_radek = pocatecni_ctverec[0]
        self.pocatecni_sloupec = pocatecni_ctverec[1]
        self.koncovy_radek = koncovy_ctverec[0]
        self.koncovy_sloupec = koncovy_ctverec[1]
        self.hybnuta_figurka = pole[self.pocatecni_radek][self.pocatecni_sloupec]
        self.sebrana_figurka = pole[self.koncovy_radek][self.koncovy_sloupec]

    def get_sachova_notace(self): # Vypíše počáteční a koncový čtverec figurky
        return self.get_horizontala_vertikala(self.pocatecni_radek, self.pocatecni_sloupec) + self.get_horizontala_vertikala(self.koncovy_radek, self.koncovy_sloupec)

    def get_horizontala_vertikala(self, radek, sloupec):
        return self.vertikala_do_sloupce[sloupec] + self.horizontala_do_radku[radek]

VYSKA_OKNA = 512  # Obrázek figurky je 64x64, 64*8 = 512
SIRKA_OKNA = 512
POCET_CTVERCU_RADEK = 8
VELIKOST_CTVERCE = VYSKA_OKNA // POCET_CTVERCU_RADEK

FIGURKY = {}


def nacist_obrazky():
    list_obrazku = ["11", "12", "13", "14", "15",
                    "16", "21", "22", "23", "24", "25", "26"]  # jmena figurek, soubory se také tak jmenují
    for obrazek in list_obrazku:
        FIGURKY[obrazek] = pygame.transform.scale(pygame.image.load(
            f"img/{obrazek}.png"), (VELIKOST_CTVERCE - 4, VELIKOST_CTVERCE - 4))  # Načtení jednotlivých obrázků


FPS = 30


def main():
    obrazovka = pygame.display.set_mode((VYSKA_OKNA, SIRKA_OKNA))
    clock = pygame.time.Clock()
    obrazovka.fill(pygame.Color(255, 255, 255))
    pole_sachy = Stav_hry()
    nacist_obrazky()  # Načíst obrázky jen jednou
    spusteno = True
    vybrany_ctverec = () # Poslední kliknutý čtverec (Řádek, sloupec)
    kliknuti_hrace = [] # Sleduje kliknutí hráče
    while spusteno:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spusteno = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pozice_mysi = pygame.mouse.get_pos() # Pozice kurzoru (x, y)
                sloupec = pozice_mysi[0] // VELIKOST_CTVERCE
                radek = pozice_mysi[1] // VELIKOST_CTVERCE
                if vybrany_ctverec == (radek, sloupec): # Když hráč zvolí stejný čtverec 2x
                    vybrany_ctverec = () # Zruší vybrání
                    kliknuti_hrace = [] # Vyčistí kliknutí
                else:
                    vybrany_ctverec = (radek, sloupec)
                    kliknuti_hrace.append(vybrany_ctverec)
                if len(kliknuti_hrace) == 2: # Po druhým kliknutí
                    pohyb = Pohyb(kliknuti_hrace[0], kliknuti_hrace[1], pole_sachy.pole)
                    print(pohyb.get_sachova_notace())
                    pole_sachy.udelej_pohyb(pohyb)
                    vybrany_ctverec = ()
                    kliknuti_hrace = []
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u: # Pokud je U stisknuto, vrátí se tah
                    pole_sachy.vratit_tah()

        vypsat_stav_hry(obrazovka, pole_sachy)
        clock.tick(FPS)
        pygame.display.flip()


# Vypisuje aktualní stav hry

def vypsat_stav_hry(obrazovka, pole_sachy):
    vypsat_ctverce(obrazovka)
    vypsat_figurky(obrazovka, pole_sachy.pole)


# Vypisuje všechny čtverce šachovnice

def vypsat_ctverce(obrazovka):
    barvy = [pygame.Color(255, 255, 255), pygame.Color(175, 175, 175)]
    for radek in range(POCET_CTVERCU_RADEK):
        for sloupec in range(POCET_CTVERCU_RADEK):
            barva = barvy[(radek + sloupec) % 2]
            pygame.draw.rect(obrazovka, barva, pygame.Rect(
                sloupec * VELIKOST_CTVERCE, radek * VELIKOST_CTVERCE, VELIKOST_CTVERCE, VELIKOST_CTVERCE))

# Vypisuje figurky pomocí aktualního stavu pole

def vypsat_figurky(obrazovka, pole_sachy):
    for radek in range(POCET_CTVERCU_RADEK):
        for sloupec in range(POCET_CTVERCU_RADEK):
            figurka = pole_sachy[radek][sloupec]
            if figurka != "30":  # Políčko není prázdný
                obrazovka.blit(FIGURKY[figurka], pygame.Rect(
                    sloupec * VELIKOST_CTVERCE, radek * VELIKOST_CTVERCE + 2, VELIKOST_CTVERCE, VELIKOST_CTVERCE))

mydb = mysql.connector.connect(
  host="dbs.spskladno.cz",
  user="student15",
  password="spsnet",
    database="vyuka15"
)

print(mydb)

if __name__ == "__main__":
    main()

pygame.quit()