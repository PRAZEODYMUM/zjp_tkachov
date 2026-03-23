"""
Zadanie:
Vráť príponu súboru (text za poslednou bodkou) v malých písmenách. Ak bodka nie je, vráť prázdny reťazec.

Vstup: nazov: názov súboru
Vystup: reťazec s príponou alebo prázdny reťazec
Priklad:
Vstup: "data.TXT"
Vystup: "txt"
"""
import os
def solve(nazov):
    extention=os.path.splitext(nazov)[1][1:]
    return extention.lower()
