def trojuhelnik(N):
    for i in range(1, N+1):
        print("*" * i)

def trojuhelnik_obracen(N):
    for i in range(N, 0, -1):
        print("*" * i)


def trojuhelnik_pravy(N):
    for i in range(N, 0, -1):
        print("{:>{}}".format("*" * i, N) )

trojuhelnik_pravy(5)