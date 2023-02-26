import math
from linearni_rce import linearni_rce

a,b,c = map(float,input("Zadej parametry rovnice ax^2 + bx + c = 0 : ").split())
print("Řeším rovnici {}x^2 {:+}x {:+} == 0".format(a,b,c))
if a == 0:
    print(linearni_rce(b,c))
else:
    D = b**2-4*a*c
    if D < 0:
        print("Nemá řešení")
    elif D == 0:
        print("Jedno řešení: ", -b/(2*a))
    else:
        print("Dvě řešení: ", [(-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a)] )