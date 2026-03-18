import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week04.task05 import solve

class TestTask05(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve(("a", "b", "c", "d"), seed=42), "a")
        self.assertEqual(solve((10, 20, 30, 40, 50), seed=7), 30)
