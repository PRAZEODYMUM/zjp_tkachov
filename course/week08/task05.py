"""
Zadanie:
Vykonaj delenie. Ak je b == 0, vráť None.

Vstup: a, b: čísla
Vystup: výsledok alebo None
Priklad:
Vstup: 10, 2
Vystup: 5
"""

def safe_divide(a, b):
    if b==0:
        return None
    else:
        return a/b