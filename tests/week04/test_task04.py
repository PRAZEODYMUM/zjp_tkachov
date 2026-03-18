import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week04.task04 import solve

class TestTask04(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve(5, 1, 10, seed=42), [2, 1, 5, 4, 4])
        self.assertEqual(solve(8, 0, 9, seed=7), [5, 2, 6, 0, 1, 8, 1, 5])
