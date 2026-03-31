"""
Zadanie:
Vytvor triedu Student s atribútmi meno a skore. Metóda passed(threshold=50) vráti True, ak skore >= threshold.

Vstup: meno: reťazec, skore: číslo
Vystup: objekt triedy Student
Priklad:
Vstup: Student("Eva", 75)
Vystup: passed() -> True
"""

class Student:
    def __init__(self, meno, skore):
        self.meno=meno
        self.skore=skore
    def passed(self, threshold=50):
        return (self.skore>threshold)