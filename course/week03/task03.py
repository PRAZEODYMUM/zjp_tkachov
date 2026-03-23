"""
Zadanie:
Priraď známku podľa skóre: A (>=90), B (>=80), C (>=70), D (>=60), E (>=50), inak FX.

Vstup: skore: celé číslo 0-100
Vystup: reťazec so známkou
Priklad:
Vstup: 90
Vystup: "A"
"""

def solve(skore):
    if (skore>=50) and (skore<60):
        return "E"
    if (skore>=60) and (skore<70):
        return "D"
    if (skore>=70) and (skore<80):
        return "C"
    if (skore>=80) and (skore<90):
        return "B"
    if (skore>=90):
        return "A"
    else:
        return "FX" 
