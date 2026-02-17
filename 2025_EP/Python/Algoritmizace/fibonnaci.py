def fibbonaci_iterativne(N):
    """
    Počítá N tý člen fibonacciho posloupnosti
    
    :param N: pozice členu

    :return: člen na N-tém místě
    """
    A = 1
    B = 1
    V = 1
    for _ in range(1, N-2+1): #-2 protože chci o dva méně koleček +1 protože tak funguje range
        V = A + B
        A = B
        B = V
    
    return V

def fibbonaci_rekurzivne(N):
    """
    Počítá N tý člen fibonacciho posloupnosti
    
    :param N: pozice členu

    :return: člen na N-tém místě
    """
    if N == 1 or N == 2:
        return 1
    
    return fibbonaci_rekurzivne(N-1) + fibbonaci_rekurzivne(N-2)


vysledek = fibbonaci_iterativne(45)
print(vysledek)

vysledek = fibbonaci_rekurzivne(45)
print(vysledek)