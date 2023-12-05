def eratosthenovo_sito(N):
    # seznam 1-N
    vysledek = list(range(1, N+1))
    # pro všechna čísla od 2 do odm(N)
    for i in range(2, int(N**(1/2))+1):
        # když je číslo v seznamu
        if i in vysledek:
            #  vyškrtavame nasobky aktualniho cisla
            for nasobek in range(i*2, N+1, i):
                if nasobek in vysledek:
                     vysledek.remove(nasobek)

    # vysledek = neskrtnute cisla
    return vysledek

print("Prvočísla jsou:", eratosthenovo_sito(51))
