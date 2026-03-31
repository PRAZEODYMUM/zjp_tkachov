"""
Zadanie:
Vypočítaj n-te Fibonacciho číslo rekurzívne (0 -> 0, 1 -> 1).

Vstup: n: celé číslo >= 0
Vystup: Fibonacciho číslo
Priklad:
Vstup: 6
Vystup: 8
"""

def solve(n):
    if n<=1:
        return n
    else:
        return solve(n-1)+solve(n-2)