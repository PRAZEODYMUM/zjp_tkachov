"""
Zadanie:
Preveď počet sekúnd na (hodiny, minúty, sekundy).

Vstup: sekundy: celé číslo
Vystup: trojica (h, m, s)
Priklad:
Vstup: 3661
Vystup: (1, 1, 1)
"""

def solve(sekundy):
    return (sekundy//3600,(sekundy%3600)//60,sekundy%60)
