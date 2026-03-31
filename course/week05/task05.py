"""
Zadanie:
Vráť prvky na párnych indexoch (0, 2, 4, ...).

Vstup: zoznam: zoznam prvkov
Vystup: zoznam prvkov z párnych indexov
Priklad:
Vstup: [0, 1, 2, 3, 4]
Vystup: [0, 2, 4]
"""

def solve(zoznam):
    par=[]
    for n in zoznam:
        if zoznam.index(n)%2==0:
            par.append(n)
    return par