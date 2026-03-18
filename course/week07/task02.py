"""
Zadanie:
Vytvor triedu Counter s počiatočnou hodnotou start. Metódy inc() a dec() menia hodnotu o 1, value() ju vráti.

Vstup: start: celé číslo (nepovinné)
Vystup: objekt triedy Counter
Priklad:
Vstup: Counter(5).inc()
Vystup: 6
"""

class Counter:
    """Jednoduchý čítač."""
    def __init__(self, start=0):
        raise NotImplementedError

    def inc(self):
        raise NotImplementedError

    def dec(self):
        raise NotImplementedError

    def value(self):
        raise NotImplementedError
