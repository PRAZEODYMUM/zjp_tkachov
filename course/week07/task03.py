"""
Zadanie:
Vytvor triedu Rectangle so šírkou a výškou. Metódy area() a perimeter() vracajú obsah a obvod.

Vstup: width, height: čísla
Vystup: objekt triedy Rectangle
Priklad:
Vstup: Rectangle(3, 4).area()
Vystup: 12
"""

class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return (self.width*self.height)
    def perimeter(self):
        return ((self.width*2)+(self.height*2))
