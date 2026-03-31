"""
Zadanie:
Vráť n, ak je kladné. Ak je n <= 0, vyhoď ValueError.

Vstup: n: celé číslo
Vystup: n alebo výnimka
Priklad:
Vstup: 3
Vystup: 3
"""

def assert_positive(n):
    if n>0:
        return n
    else:
        raise ValueError
