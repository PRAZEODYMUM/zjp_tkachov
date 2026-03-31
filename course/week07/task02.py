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
    def __init__(self, start=0):
        self.start=start
    def inc(self):
        self.start+=1
        return self.start
    def dec(self):
        self.start-=1
        return self.start
    def value(self):
        return self.start