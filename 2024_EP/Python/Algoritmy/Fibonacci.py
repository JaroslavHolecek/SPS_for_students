def fibonacci_iter(n):
    A = 1
    B = 1
    C = 1
    pocet = 1

    while pocet < n:
        C = A + B
        pocet += 1
        A = B
        B = C
    
    return C

def fibonacci_rekurze(n_zelene):
    if n_zelene == 0 or n_zelene == 1:
        return 1 # cerne
    
    return fibonacci_rekurze(n_zelene-1) + fibonacci_rekurze(n_zelene-2)


vysledek = fibonacci_iter(n=50)
print(vysledek)
vysledek = fibonacci_rekurze(n_zelene=50)
print(vysledek)

