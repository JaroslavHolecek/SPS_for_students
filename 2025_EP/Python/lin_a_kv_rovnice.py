def linearni_rovnice_neprehledne(a, b):
    if a == 0:
        # v a je uložená nula
        if b == 0:
            # v b je uložená nula
            return "Nekonečně mnoho řešení"
        else:
            # v b není uložená nula
            return "Nemá řešení"
    else:
        # v a není uložená nula
        return -b/a
    
def linearni_rovnice(a, b):
    """
    Řeší rovnici ax + b = 0 
    
    :param a: koeficient u x
    :param b: absolutní člen

    :return: hodnotu x 
    """
    if a == 0 and b != 0:
        return "Nemá řešení"
    
    if a == 0 and b == 0:
        return "Nekonečně mnoho řešení"
        
    return -b/a
    

def kvadraticka_rce(a, b, c):
    """
    Řeší rovnici ax^2 + bx + c
    
    :param a: koeficient kvadratického členu
    :param b: koeficient lineárního členu
    :param c: absolutní člen

    :return: Hodnota x
    """
    if a == 0:
        return linearni_rovnice(b, c)
    
    D = b**2 - 4*a*c

    if D < 0:
        return "Nemá řešení"

    if D == 0:
        return -b / (2*a)
        
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    return x1, x2


vysledek = linearni_rovnice(0, 0)
print(vysledek)

vysledek = kvadraticka_rce(-14, 3, 7)
print(vysledek)




