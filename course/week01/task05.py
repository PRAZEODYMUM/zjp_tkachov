"""
Zadanie:
Vráť True, ak text obsahuje slovo "anaconda" bez ohľadu na veľkosť písmen.

Vstup: text: reťazec
Vystup: True alebo False
Priklad:
Vstup: "AnAcoNda je super"
Vystup: True
"""

def solve(text):
    if 'anaconda' in text.lower():
        return True
    else:
        return False
