def linearni_jako_text(a,b):
    # return f"{a}x {b:+} = 0" # není úplně dokonalé...
    a_text = '' if a==0 else f'{a}x' # stejné jako běžný if, jen napsané do jednoho řádku

    if a_text == '':
        b_text = f"{b}"
    else:
        b_text = '' if b==0 else f"{b:+}"
    return f"{a_text} {b_text} = 0"

def linearni_rovnice(a,b):
    if a != 0:
        return -b/a
    else:
        if b == 0:
            return "celé R"
        else:
            return "nemá řešení"

def kvadraticka_rovnice(a,b,c):
    print(f"{a}x^2 {b:+}x {c:+} = 0") # lepší zobrazení kvadaratické rovnice si zkuste jako cvičení... viz fce linearni_jako_text()
    if a == 0:
        return linearni_rovnice(b,c)
    else:
        D = b**2 - 4 * a * c
        if D < 0 :
            return "nemá řešení"
        elif  D == 0 :
            return -b / (2 * a)
        else:
            return [(-b + D**(1/2)) / (2*a), (-b - D**(1/2)) / (2*a) ]

print(linearni_jako_text(3,-5), "výsledek:", linearni_rovnice(3, -5))
print(linearni_jako_text(0,5), "výsledek:", linearni_rovnice(0, 5))
print(linearni_jako_text(3,0), "výsledek:", linearni_rovnice(3, 0))
print(linearni_jako_text(0,0), "výsledek:", linearni_rovnice(0, 0))

print (kvadraticka_rovnice(1, 3, 7))