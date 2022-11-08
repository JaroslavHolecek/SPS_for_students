# https://docs.scipy.org/doc/scipy/tutorial/index.html
import numpy as np
from scipy.optimize import LinearConstraint, milp

mnozstvi_medunka = 1000
mnozstvi_mata = 1500

v_balicku = 100
medunky_ve_smesi = 70
maty_ve_smesi = v_balicku - medunky_ve_smesi

zisk_medunka = 10
zisk_mata = 20
zisk_smes = 15

# - protože scipy.milp minimalizuje
#                 x,            y,         z -> počty balíčků
zisk = -np.array([zisk_medunka, zisk_mata, zisk_smes])

horni_limit = np.array([mnozstvi_medunka, mnozstvi_mata, np.inf])
spodni_limit = np.array([0,0,0])

uloha_A = np.array([[v_balicku,0,medunky_ve_smesi],
                    [0,v_balicku,maty_ve_smesi],
                    [1,1,1]])

omezeni = LinearConstraint(uloha_A, spodni_limit, horni_limit)
celociselnost = np.array([1, 1, 1])

vysledek = milp(c=zisk, constraints=omezeni, integrality=celociselnost)
print(vysledek.x)
print(vysledek)