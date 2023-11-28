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

print ("Prvočísla", Eratosthenovo_sito(100))

print("Lichá:", *range(1,100,2))
print("Sudá:", *range(2,100+1,2))
print("Názobky tří pozpátku:", *range(99,0,-3))
