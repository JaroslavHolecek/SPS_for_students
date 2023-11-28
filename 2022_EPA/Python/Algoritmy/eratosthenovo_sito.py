def eratosthenovo_sito(N):

    # seznam 1-N
    vysledek = list(range(1, N+1))

    # pro všechna čísla od 2 do odm(N)
    for i in range(2, int(N**(1/2))): # +1
        # když je číslo v seznamu
        if i in vysledek:
            #  vyškrtavame nasobky aktualniho cisla
            for nasobek in range(i*2, N+1, i):
                if nasobek in vysledek:
                     vysledek.remove(nasobek)

    # vysledek = neskrtnute cisla
    return vysledek

print(56**(1/2), int(56**(1/2)), *range(2, int(56**(1/2))) )
print(*range(5, 21, 3))
print("Prvočísla jsou:", eratosthenovo_sito(81))
