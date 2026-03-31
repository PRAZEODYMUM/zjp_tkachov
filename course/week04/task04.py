"""
Zadanie:
Vygeneruj n náhodných celých čísel z intervalu <a, b>. Použi random.seed(seed).

Vstup: n: počet, a, b: hranice, seed: celé číslo
Vystup: zoznam náhodných čísel
Priklad:
Vstup: 5, 1, 10, seed=42
Vystup: [2, 1, 5, 4, 4]
"""

import random

def solve(n, a, b, seed=0):
    li=[]
    random.seed(seed)
    i=1
    while i<=n:
        li.append(random.randint(a,b))
        i+=1
    return li