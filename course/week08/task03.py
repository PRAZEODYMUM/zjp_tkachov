"""
Zadanie:
Vytvor dekorátor, ktorý pridá prefix k reťazcovému výsledku funkcie.

Vstup: prefix: reťazec
Vystup: dekorátor
Priklad:
Vstup: @prefix_text("Ahoj ") na funkcii meno("Eva")
Vystup: "Ahoj Eva"
"""

def prefix_text(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return prefix + func(*args, **kwargs)
        return wrapper
    return decorator