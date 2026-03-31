"""
Zadanie:
Over, či je text palindróm. Ignoruj medzery a veľkosť písmen.

Vstup: text: reťazec
Vystup: True alebo False
Priklad:
Vstup: "Kobyla ma maly bok"
Vystup: True
"""

def is_palindrome(text='Kobyla ma maly bok'):
    low=(text.lower()).replace(' ','')
    return (low==low[::-1])