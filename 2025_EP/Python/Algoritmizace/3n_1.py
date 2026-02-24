def triN_plus_jedna(N):
    """
    Vrátí seznam všech mezi výsledků, včetně počátečního čísla pro Collatzův problém (3n+1) a také počet kroků potřebných pro dosažení konečné 1
    """

    krok = 0
    posloupnost = [N]
    while N > 1:
        N = N // 2 if N % 2 == 0 else N*3+1
        krok += 1
        posloupnost.append(N)
    return posloupnost, krok

vstup = int(input("Zadej číslo:"))
rada, kroku = triN_plus_jedna(vstup)
print(f"Pro číslo {vstup} je počet kroků {kroku} a řada {rada}")
