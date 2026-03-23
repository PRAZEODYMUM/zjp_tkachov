"""
Zadanie:
Zisti, či je rok priestupný (deliteľný 4, nie 100, okrem deliteľných 400).

Vstup: rok: celé číslo
Vystup: True alebo False
Priklad:
Vstup: 2000
Vystup: True
"""

def solve(rok):
    return rok%4==0 and (rok%100!=0 or rok%400==0)
