def triNplusJedna(X):
    pocitadlo = 0

    while X > 1:
        print(f"Aktualni X: {X}")
        pocitadlo += 1
        if X % 2 == 0: # sude
            X = X // 2
        else: # liche
            X = X*3 + 1 

    return pocitadlo

print(f"Pocet vypoctu byl: {triNplusJedna(50)}")