def fibbonaci_rekursivne(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibbonaci_rekursivne(n-1) + fibbonaci_rekursivne(n-2)

def fibbonaci_interativne(n):
    prvni = 0
    druhe = 1
    for poradi in range(2, n+1):
        dalsi = prvni + druhe
        prvni = druhe
        druhe = dalsi
    return dalsi

print (fibbonaci_interativne(100))
print(fibbonaci_rekursivne(100))
