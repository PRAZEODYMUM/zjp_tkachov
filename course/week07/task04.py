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
    def sound(self):
        return 'ticho'
class Dog(Animal):
    def sound(self):
        return 'haf'
