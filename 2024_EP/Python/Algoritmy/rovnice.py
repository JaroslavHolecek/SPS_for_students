def linarni_rce(a, b):
    """
    Řeší lineární rovnici ve tvaru ax + b = 0.
    Args:
        a (float): Koeficient u proměnné x
        b (float): Absolutní člen
    Returns:
        float or str: Řešení rovnice (x = -b/a) pokud existuje jediné řešení,
                      "Nekonečně mnoho řešení" pokud a = 0 a b = 0,
                      "Námá řešení" pokud a = 0 a b ≠ 0
    """

    if a == 0 and b == 0:
        return "Nekonečně mnoho řešení"
    
    if a == 0 and b != 0:
        return "Nemá řešení"

    return -b/a  

def kvadraticka_rce(a, b, c):
    """
    Solves a quadratic equation of the form ax² + bx + c = 0.
    Args:
        a (float): Coefficient of x² term
        b (float): Coefficient of x term
        c (float): Constant term
    Returns:
        list or str: 
            - If a == 0, calls linarni_rce(b, c) for linear equation
            - If discriminant < 0, returns "Nemá řešení" (no solution)
            - If discriminant == 0, returns list with one solution (double root)
            - If discriminant > 0, returns list with two solutions [x1, x2]
    Examples:
        >>> kvadraticka_rce(1, -3, 2)  # x² - 3x + 2 = 0
        [2.0, 1.0]
        >>> kvadraticka_rce(1, 0, 1)   # x² + 1 = 0
        "Nemá řešení"
    """
    if a == 0:
        return linarni_rce(b, c)
    
    D = b**2 - 4*a*c

    if D < 0:
        return "Nemá řešení"
    
    if D == 0:
        return [ -b / (2*a) ]
    
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    
    return [x1, x2]
    

    

A = 1
B = 5
C = 2
vysledek = kvadraticka_rce(A, B, C)
print(f"Pro vstup {A} a {B} a {C} je řešení {vysledek}")
    