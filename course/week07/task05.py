"""
Zadanie:
Vytvor triedu BankAccount s metódami deposit, withdraw a get_balance.

Vstup: owner: reťazec, balance: číslo (nepovinné)
Vystup: objekt triedy BankAccount
Priklad:
Vstup: BankAccount("Eva").deposit(100)
Vystup: 100
"""

class BankAccount:
    """Jednoduchý bankový účet."""
    def __init__(self, owner, balance=0):
        raise NotImplementedError

    def deposit(self, amount):
        raise NotImplementedError

    def withdraw(self, amount):
        raise NotImplementedError

    def get_balance(self):
        raise NotImplementedError
