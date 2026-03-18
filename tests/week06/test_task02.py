import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week06.task02 import solve

class TestTask02(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve(0), 0)
        self.assertEqual(solve(1), 1)
        self.assertEqual(solve(6), 8)
