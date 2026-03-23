"""
Zadanie:
Nahraď všetky spätné lomky \ za / v zadanom texte.

Vstup: cesta: reťazec
Vystup: reťazec s lomkami /
Priklad:
Vstup: "D:\projekty\skola"
Vystup: "D:/projekty/skola"
"""

def solve(cesta):
    return cesta.replace('\\','/')
