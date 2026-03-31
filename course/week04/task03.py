"""
Zadanie:
Vráť zoznam unikátnych prvkov v pôvodnom poradí.

Vstup: polozky: zoznam
Vystup: zoznam bez duplicít
Priklad:
Vstup: [1, 2, 1, 3, 2]
Vystup: [1, 2, 3]
"""

def solve(polozky):
    m=[]
    seen=set()
    for n in polozky:
        if n not in seen:
            seen.add(n)
            m.append(n)
    return m