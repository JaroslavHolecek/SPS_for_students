def f(x):
    """Funkce f vrací hodnotu x na třetí plus jedna.
    Args:
        x (int, float): číslo, pro které se počítá hodnota funkce
    Returns:
        int, float: hodnota funkce f pro zadané x
    """
    vysledek = x**3 + 1
    return vysledek


print(f"Výsledek funkce f pro x=2 je: {f(2)}")
print(f"Výsledek funkce f pro x=3 je: {f(3)}")
print(f"Výsledek funkce f pro x=1 je: {f(1)}")
print(f"Výsledek funkce f pro x=-1 je: {f(-1)}")

def zmena_promenne(p):
    """Funkce zmena_promenne změní hodnotu proměnné p uvnitř funkce a vrátí destinásobek.
    Args:
        p (int): původní hodnota proměnné
    Returns:
        int: nová hodnota proměnné
    """
    print(f"Hodnota p uvnitř funkce před změnou: {p}")
    p = 10
    return p*10

promenna = 5
print(f"Hodnota proměnné před voláním funkce: {promenna}")
zmena_promenne(promenna)
print(f"Hodnota proměnné po volání funkce: {promenna}")

def zmena_pole(pole):
    """Funkce zmena_pole změní první prvek pole na 10.
    Args:
        pole (list): původní pole
    Returns:
        None
    """
    print(f"Hodnota pole uvnitř funkce před změnou: {pole}")
    pole[0] = 10
    print(f"Hodnota pole uvnitř funkce po změně: {pole}")

pole = [1, 2, 3]
print(f"Hodnota pole před voláním funkce: {pole}")
zmena_pole(pole)
print(f"Hodnota pole po volání funkce: {pole}")
