def euklid(A, B):
    """
    Spočítá největrší společný dělitel
    
    :param A: vstup 1
    :param B: vstup 2

    :return: NSD A a B
    """
    while not B == 0:
        Z = A % B
        A = B
        B = Z
    
    return A

vysledek = euklid(125, 500)
print(vysledek)