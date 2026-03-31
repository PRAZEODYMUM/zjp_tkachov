"""
Zadanie:
Vytvor dekorátor, ktorý zdvojnásobí návratovú hodnotu funkcie.

Vstup: func: funkcia
Vystup: obalená funkcia
Priklad:
Vstup: @double_result na funkcii add(2, 3)
Vystup: 10
"""

def double_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper