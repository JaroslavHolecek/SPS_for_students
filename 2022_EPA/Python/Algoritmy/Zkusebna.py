# Komentář - sem si můžu psát co chci
def triNplusJedna(x):
    while x > 1:
        print(x)
        if x%2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1



triNplusJedna(100)
triNplusJedna(10)
triNplusJedna(25)