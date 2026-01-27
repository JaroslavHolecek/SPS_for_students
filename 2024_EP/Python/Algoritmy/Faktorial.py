def faktorial_iter(n):
    """
    Spočítá faktoriál vstupní hodnoty pomocí iterativního postupu
    
    :param n: hodnota pro kterou se spočítá faktoriál

    :return : faktoriál vstupní hodnoty
    """
    vysledek = 1
    for cislo in range(1, n+1):
        vysledek = cislo * vysledek

    return vysledek

def faktorial_rekurze(n):
    """
    Spočítá faktoriál vstupní hodnoty pomocí rekurze
    
    :param n: hodnota pro kterou se spočítá faktoriál

    :return : faktoriál vstupní hodnoty
    """
    if n <= 0:
        return "nevhodný vstup"
    
    if n == 1:
        return 1
    
    return n * faktorial_rekurze(n-1)




vysledek = faktorial_iter(n=6)
print(vysledek)

vysledek = faktorial_rekurze(n=6)
print(vysledek)

