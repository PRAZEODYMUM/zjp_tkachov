"""
Zadanie:
Vytvor triedu Animal so metódou sound(), ktorá vráti "ticho". Vytvor triedu Dog(Animal), ktorá vráti "haf".

Vstup: žiadny
Vystup: objekty tried Animal a Dog
Priklad:
Vstup: Dog().sound()
Vystup: "haf"
"""

class Animal:
    """Základné zviera."""
    def sound(self):
        raise NotImplementedError


class Dog(Animal):
    """Pes."""
    def sound(self):
        raise NotImplementedError
