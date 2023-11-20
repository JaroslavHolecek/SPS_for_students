def MinZeTri (x,y,z):
    if x < y :
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z

def MaxZeTri (x,y,z):
    if x > y :
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z


def minpole (p):
    nej = p[0]
    for prvek in p:
        if prvek < nej:
            nej = prvek
    return nej


def maxpole (p):
    nej = p[0]
    for prvek in p:
        if nej < prvek:
            nej = prvek
    return nej


print("nejvetsi je", maxpole([1,5,7,2,8,2.1]))
print("nejvetsi je", maxpole([8,6,4,2,25,4]))
print("nejmensi je", minpole([1,5,7,2,8,2.1]))
print("nejmensi je", minpole([8,6,4,2,25,4]))
print("nejvetsi je", MaxZeTri(5,8,4))
print("nejvetsi je", MaxZeTri(1,6,2))
print("nejvetsi je", MaxZeTri(9,4,5))