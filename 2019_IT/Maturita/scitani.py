print(__name__)
def scitani_tri(a,b,c):
    return a + b + c

if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    ocekavany_vysledek = 6
    vysledek = scitani_tri(a,b,c)
    if ocekavany_vysledek == vysledek:
        print("OK")
    else:
        print(f"Výsledek {vysledek} vs. očekáváno {ocekavany_vysledek}")
    
    
    a = 1
    b = 2
    c = 0
    ocekavany_vysledek = 3
    vysledek = scitani_tri(a,b,c)
    if ocekavany_vysledek == vysledek:
        print("OK")
    else:
        print(f"Výsledek {vysledek} vs. očekáváno {ocekavany_vysledek}")
    
    
    
