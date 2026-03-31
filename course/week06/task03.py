"""
Zadanie:
Zorad zoznam dvojíc podľa druhého prvku pomocou lambda výrazu.

Vstup: dvojice: zoznam dvojíc
Vystup: zoradený zoznam
Priklad:
Vstup: [(1, 3), (2, 2), (3, 1)]
Vystup: [(3, 1), (2, 2), (1, 3)]
"""

def solve(dvojice):
    srt=sorted(dvojice,key=lambda x: x[1])
    return srt