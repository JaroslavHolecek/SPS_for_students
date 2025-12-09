def euklid(a, b):
    while not (a == 0 or b == 0):
        if a > b:
            a = a - b
        else:
            b = b - a
    if a == 0:
        return b
    else:
        return a

def euklid_modulo(a, b):
    while not b == 0:
        z = a % b
        a = b
        b = z
    return a




print("Největší společný dělitel je:", euklid(125, 25))
print("Největší společný dělitel je:", euklid(11475896, 478952))

print("Největší společný dělitel je:", euklid_modulo(125, 25))
print("Největší společný dělitel je:", euklid_modulo(11475896, 478952))