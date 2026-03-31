"""
Zadanie:
Použi vnorenú funkciu na výpočet (x + 1) na druhú.

Vstup: x: číslo
Vystup: výsledok (x + 1)^2
Priklad:
Vstup: 2
Vystup: 9
"""

def solve(x):
    sqr=lambda x: x**2
    return sqr(x+1)