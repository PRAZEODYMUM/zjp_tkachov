import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week04.task02 import solve

class TestTask02(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve([1, 2, 3]), [1, 4, 9])
        self.assertEqual(solve([]), [])
