import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week06.task05 import solve

class TestTask05(unittest.TestCase):
    def test_main(self):
        f = solve(3)
        self.assertEqual(f(4), 12)
        g = solve(-2)
        self.assertEqual(g(5), -10)
