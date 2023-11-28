def min_ze_tri(x,y,z):
    p = x
    if p > y:
        p = y
    if p > z:
        p = z
    return p

def max_ze_tri(x,y,z):
    p = x
    if p < y:
        p = y
    if p < z:
        p = z
    return p

print("nejmensi je",min_ze_tri(5,10,15) )
print("nejvetsi je",max_ze_tri(5,10,15) )


def min_v_poli(pole):
    min_hodnota = pole[0]
    for prvek in pole:
        if prvek < min_hodnota:
            min_hodnota = prvek
    return min_hodnota

def max_v_poli(pole):
    max_hodnota = pole[0]
    for prvek in pole:
        if prvek > max_hodnota:
            max_hodnota = prvek
    return max_hodnota

print(min_v_poli([5, 2, -45, 78, 10000000000, 0]))