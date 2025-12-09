def Hornerovo_schema (koeficienty, x):
    vysledek = 0
    for i in koeficienty[:-1]: # všechny koeficienty kromě posledního
        vysledek = (vysledek + i) * x

    vysledek = vysledek + koeficienty[-1] # poslední koeficient přičítáme

    return vysledek

print(Hornerovo_schema(koeficienty=[10, 4, -2, -1, 1, 5], x=8))