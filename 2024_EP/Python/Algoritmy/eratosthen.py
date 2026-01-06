def prvocisla(N):
    """
    Najde všechna prvočísla od 1 do N
    
    :param N: horní limit rozsahu

    return
    list: prvočísla 1 - N
    """

    rada_cisel = [*range(1, N+1)]
    print(rada_cisel)

    for cislo in range(2, int(N**0.5)+1): # od 2 do odmocniny z N
        if cislo not in rada_cisel:
            continue

        for nasobek in range(2*cislo, N+1, cislo): # násobky cisla
            if nasobek in rada_cisel:
                rada_cisel.remove(nasobek)

    return rada_cisel



print(prvocisla(100))