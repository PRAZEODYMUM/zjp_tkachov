"""
Zadanie:
Vypočítaj kĺzavý priemer s dĺžkou okna window. Ak okno nepasuje, vráť prázdny zoznam.

Vstup: data: zoznam čísel, window: celé číslo
Vystup: zoznam priemerov
Priklad:
Vstup: [1, 2, 3, 4], 2
Vystup: [1.5, 2.5, 3.5]
"""
import numpy as np
def solve(data, window):
    if window>len(data):
        return []
    result=[]
    for i in range((len(data)-window)+1):
        avg=float(np.average(data[i:i+window]))
        result.append(avg)
    return result