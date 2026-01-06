def eukliduv_algoritmus(A, B):
    """
    Počítá NSD pomocí Euklidova algoritmu (zbytek po celočíselném dělení)
    
    :param A (int or float): První číslo pro společný dělitel
    :param B (int or float): Druhé číslo pro společný dělitel

    Returns:
        int or float: NSD čísel A a B
    """
    while not B == 0: # to stejné jako B != 0
        C = A % B # výpočet a uložení zbytku po dělení
        A = B # posun hodnot
        B = C

    return A
    

    
print(f"Výsledek je {eukliduv_algoritmus(15, 23)}")