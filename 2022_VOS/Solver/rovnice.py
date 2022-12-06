from scipy import optimize as op
import math

def equations(p):
    x, y = p
    return (x+y**2-4, math.exp(x) + x*y - 3)

x, y =  op.fsolve(equations, (1, 1))

print( equations((x, y)) )
print(x,y)