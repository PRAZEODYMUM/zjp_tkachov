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
    """Reprezentuje študenta s menom a skóre."""
    def __init__(self, meno, skore):
        raise NotImplementedError

    def passed(self, threshold=50):
        raise NotImplementedError
