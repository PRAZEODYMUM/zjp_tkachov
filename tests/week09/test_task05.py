import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week09.task05 import solve

class TestTask05(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve([1, 2, 3, 4], 2), [1.5, 2.5, 3.5])
        self.assertEqual(solve([1, 2, 3, 4], 4), [2.5])
        self.assertEqual(solve([1, 2, 3, 4], 5), [])
