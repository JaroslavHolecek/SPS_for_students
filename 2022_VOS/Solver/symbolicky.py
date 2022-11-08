# https://docs.sympy.org/latest/tutorials/
from sympy import *


x, y = symbols('x, y')
eq1 = Eq(x+y**2, 4)
eq2 = Eq(x**2 + y, 4)

sol = solve([eq1, eq2], [x, y])

print(sol)
pprint(sol)