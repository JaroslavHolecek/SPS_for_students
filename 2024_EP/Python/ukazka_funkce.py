def overeni(vek: int) -> str:
    """Funkce pro ověření věku.
    
    Args:
        vek (int): Věk uživatele.

    Returns:
        str: Výsledek ověření věku.
    """
    assert type(vek) is int, "Věk musí být celé číslo"
    assert vek >= 0, "Věk musí být nezáporné číslo"

    print("Věk je:", vek)
    limit = 18 # limit plnoletosti
    print("Limit je:", limit)
    if vek >= limit:
        return "Vstup povolen"
    
    if vek >= 15:
        return "Vstup povolen s omezením"

    return "Vstup zakázán"


vysledek = overeni(vek="Dvacet")
print(vysledek)
overeni(vek=18)
overeni(vek=16)
overeni(vek=15)
overeni(vek=10)
