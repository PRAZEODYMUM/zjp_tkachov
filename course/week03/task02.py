"""
Zadanie:
Vráť maximum z troch čísel pomocou if/else.

Vstup: a, b, c: čísla
Vystup: najväčšie číslo
Priklad:
Vstup: 1, 2, 3
Vystup: 3
"""

def solve(a, b, c):
    max=None
    if a>b:
        max=a
    else:
        max=b
    if c>max:
        max=c
    return max
