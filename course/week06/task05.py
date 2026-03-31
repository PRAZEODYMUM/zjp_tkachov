"""
Zadanie:
Vytvor a vráť funkciu, ktorá násobí vstup hodnotou k (closure).

Vstup: k: číslo
Vystup: funkcia, ktorá násobí vstup hodnotou k
Priklad:
Vstup: k=3, potom f(4)
Vystup: 12
"""

def solve(k):
    mtp=lambda x: x*k
    return mtp