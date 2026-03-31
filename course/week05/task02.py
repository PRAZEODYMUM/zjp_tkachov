"""
Zadanie:
Spočítaj samohlásky (a, e, i, o, u, y) bez ohľadu na veľkosť písmen.

Vstup: text: reťazec
Vystup: počet samohlások
Priklad:
Vstup: "Python"
Vystup: 2
"""

def solve(text):
    samohlasky={'a','e','i','o','u','y'}
    i=0
    for n in text:
        if n.lower() in samohlasky:
            i+=1
    return i