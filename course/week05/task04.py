"""
Zadanie:
Spočítaj hodnoty v slovníku (sumu všetkých hodnôt).

Vstup: slovnik: slovník s číselnými hodnotami
Vystup: súčet hodnôt
Priklad:
Vstup: {"a": 1, "b": 2}
Vystup: 3
"""

def solve(slovnik):
    return sum(slovnik.values())