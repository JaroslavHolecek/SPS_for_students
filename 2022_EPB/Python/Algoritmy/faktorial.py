def faktorial_interativne(N):
    vysledek=1
    for cislo in range(1,N+1):
        vysledek=vysledek * cislo
    return vysledek

print(faktorial_interativne(5))
print(faktorial_interativne(20))


def faktorial_rekurzivne(N):
    if N == 0:
        return 1
    return N * faktorial_rekurzivne(N - 1)

print(faktorial_rekurzivne(5))
