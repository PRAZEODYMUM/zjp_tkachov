"""
Zadanie:
Spočítaj hodnoty v zozname pomocou cyklu.

Vstup: cisla: zoznam čísel
Vystup: súčet
Priklad:
Vstup: [1, 2, 3]
Vystup: 6
"""

def solve(cisla):
    sum=0
    for n in cisla:
        sum+=n
    return sum