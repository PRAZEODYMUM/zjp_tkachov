"""
Zadanie:
Normalizuj dáta do rozsahu 0-1. Ak sú všetky hodnoty rovnaké, vráť samé nuly.

Vstup: data: zoznam čísel
Vystup: zoznam normalizovaných hodnôt
Priklad:
Vstup: [2, 4, 6]
Vystup: [0.0, 0.5, 1.0]
"""

def solve(data):
    if not data:
        return []
    min_val=min(data)
    max_val=max(data)
    if min_val==max_val:
        return [0.0]*len(data)
    return [(x-min_val)/(max_val-min_val) for x in data]