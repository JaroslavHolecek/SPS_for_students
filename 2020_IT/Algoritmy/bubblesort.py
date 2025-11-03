sort = [5,3,61,65,33, 8,4,7,5,9,4,6,1,2,3]
def bubble(pole):
    N = len(pole)
    pocitadlo_kroku = 0
    for velke_kolo in range(N-1): #toto opakovat (bez posledního čísla, N-1x)
        for dvojice in range(N-1-velke_kolo): #postupně se všemi dvojcemi
            # vzít 2 čísla a porovnat je, prohodit
            pocitadlo_kroku+=1
            a = pole[dvojice]
            b = pole[dvojice+1]
            if a>b:
                pole[dvojice] = b
                pole[dvojice+1] = a
    print(pocitadlo_kroku)

print(sort)
bubble(sort)
print(sort)
bubble(sort)
print(sort)
