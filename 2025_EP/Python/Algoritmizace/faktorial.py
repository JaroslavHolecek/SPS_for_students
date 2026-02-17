def nasobeni_do_N(N):
    """
    Počítá faktoriál N
    
    :param N: hodnota pro výpočet jejího faktoriálu

    :return: N!
    """
    V = 1
    for c in range(1, N+1):
        V = V * c
    
    return V

def fakt_rekurzivne(N):
    """
    Počítá faktoriál N
    
    :param N: hodnota pro výpočet jejího faktoriálu

    :return: N!
    """
    if N == 1:
        return 1
    
    return N * fakt_rekurzivne(N-1)


vysledek = nasobeni_do_N(54)
print(vysledek)

vysledek = fakt_rekurzivne(54)
print(vysledek)