def hornerovo_schema(koef:list, x):
    """
    Počítá hodnoty polynomu pro zadané X
    """
    vysledek = 0

    for k in koef:
        vysledek = vysledek + k
        vysledek = vysledek * x
    
    vysledek = vysledek / x

    return vysledek


hodnota = hornerovo_schema(koef=[5, 3, -8], x=3)
print(hodnota)
