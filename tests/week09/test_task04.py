import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week09.task04 import solve

class TestTask04(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve([2, 4, 6]), [0.0, 0.5, 1.0])
        self.assertEqual(solve([5, 5]), [0.0, 0.0])
        self.assertEqual(solve([]), [])
