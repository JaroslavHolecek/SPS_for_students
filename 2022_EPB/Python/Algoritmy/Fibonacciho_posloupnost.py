def fibonacci_iterativne (N):
    prvni = 0
    druhe = 1
    for p in range (2, N+1):
        dalsi = prvni + druhe
        prvni = druhe
        druhe = dalsi
    return dalsi

print(fibonacci_iterativne(42))


def fibonacci_rekursivne (N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return fibonacci_rekursivne(N - 1) + fibonacci_rekursivne(N - 2)



fibonacci_rekursivne(6)