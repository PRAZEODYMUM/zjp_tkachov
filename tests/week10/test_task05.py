import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week10.task05 import solve

class TestTask05(unittest.TestCase):
    def test_main(self):
        slope, intercept = solve([0, 1, 2], [0, 2, 4])
        self.assertAlmostEqual(slope, 2.0)
        self.assertAlmostEqual(intercept, 0.0)
