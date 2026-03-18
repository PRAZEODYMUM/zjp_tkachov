import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week07.task05 import BankAccount

class TestTask05(unittest.TestCase):
    def test_main(self):
        acc = BankAccount("Eva")
        self.assertEqual(acc.get_balance(), 0)
        acc.deposit(100)
        self.assertEqual(acc.get_balance(), 100)
        self.assertTrue(acc.withdraw(30))
        self.assertEqual(acc.get_balance(), 70)
        self.assertFalse(acc.withdraw(100))
        self.assertEqual(acc.get_balance(), 70)
