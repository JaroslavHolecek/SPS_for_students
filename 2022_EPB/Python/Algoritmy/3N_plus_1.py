def trinplusjedna(N):
    pocitadlo = 0
    while 1 < N:
       print("Aktuální N:", N)
       pocitadlo = pocitadlo + 1
       if N%2 != 0:
           N = N*3 + 1
       else:
           N = N//2
    print("Konec", pocitadlo)


trinplusjedna(1294578923415)