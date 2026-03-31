"""
Zadanie:
Vypočítaj faktoriál rekurzívne.

Vstup: n: celé číslo >= 0
Vystup: faktoriál
Priklad:
Vstup: 5
Vystup: 120
"""

def solve(n):
    if n<1:
        return 1
    else:
        return n*solve(n-1)