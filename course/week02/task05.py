"""
Zadanie:
Spočítaj súčet číslic v reťazci.

Vstup: cisla: reťazec obsahujúci iba číslice
Vystup: súčet číslic
Priklad:
Vstup: "1203"
Vystup: 6
"""

def solve(cisla):
    zoznam=list(cisla)
    sucet=sum(int(n) for n in zoznam)
    return sucet
