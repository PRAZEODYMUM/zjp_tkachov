"""
Zadanie:
Vypočítaj súčin všetkých prvkov v n-tici.

Vstup: cisla: n-tica čísel
Vystup: súčin (ak je n-tica prázdna, vráť 1)
Priklad:
Vstup: (2, 3, 4)
Vystup: 24
"""

def solve(cisla):
    i=1
    for n in cisla:
        i*=n
    return i