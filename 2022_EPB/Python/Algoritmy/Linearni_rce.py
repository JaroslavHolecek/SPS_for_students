def linearni_rovnice(a, b):
    print(f'{a}x {b:+} == 0')
    if a == 0:
        if b ==0:
            return "Celé R"
        else:
            return "Nemá řešní"
    else:
        return -b/a


def kvadraticka_rovnice(a,b,c):
    if a == 0:
        return linearni_rovnice(b,c)
    else:
        D=b**2-4*a*c
        if D==0:
            return -b/(2*a)
        elif D<0:
            return "nemá řešení"
        else:
            return [(-b+D**(1/2))/(2*a),
                    (-b - D ** (1 / 2)) / (2 * a)]


print(kvadraticka_rovnice(2, 0, 6))
print(kvadraticka_rovnice(0, -5, 2))
print(kvadraticka_rovnice(9, -6, -3))
print(linearni_rovnice(7, -6))
print(linearni_rovnice(0, 0))