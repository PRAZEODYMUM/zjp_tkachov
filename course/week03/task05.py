"""
Zadanie:
Over, či z troch strán vznikne trojuholník (sú kladné a súčet dvoch je väčší než tretia).

Vstup: a, b, c: dĺžky strán
Vystup: True alebo False
Priklad:
Vstup: 3, 4, 5
Vystup: True
"""

def solve(a, b, c):
    if (a*(-1)<0 and b*(-1)<0 and c*(-1)<0) and (a+b>c and a+c>b and b+c>a):
        return True
    else:
        return False
