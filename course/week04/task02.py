"""
Zadanie:
Vytvor nový zoznam so štvorcami hodnôt.

Vstup: cisla: zoznam čísel
Vystup: zoznam štvorcov
Priklad:
Vstup: [1, 2, 3]
Vystup: [1, 4, 9]
"""

def solve(cisla):
    m=[]
    for n in cisla:
        m.append(n**2)
    return m