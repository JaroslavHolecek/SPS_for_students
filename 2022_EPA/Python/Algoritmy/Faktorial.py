def faktorial_iterativne(n):
    vysledek = 1
    for i in range(1, n+1):
        vysledek = vysledek*i
    return vysledek

print(faktorial_iterativne(5))

def faktorial_rekurzivne(n):
    if n == 0:
        return 1
    return n * faktorial_rekurzivne(n - 1)

print(faktorial_rekurzivne(5))