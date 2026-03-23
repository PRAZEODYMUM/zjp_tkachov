"""
Zadanie:
Vráť True, ak je číslo kladné a párne.

Vstup: n: celé číslo
Vystup: True alebo False
Priklad:
Vstup: 4
Vystup: True
"""

def solve(n):
    if (n*(-1)>0) or (n%2!=0):
        return False
    else:
        return True
