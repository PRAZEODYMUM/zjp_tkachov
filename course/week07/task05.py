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
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self.balance
    def withdraw(self, amount):
        if amount>self.balance:
            return False
        self.balance-=amount
        return self.balance
    def get_balance(self):
        return self.balance