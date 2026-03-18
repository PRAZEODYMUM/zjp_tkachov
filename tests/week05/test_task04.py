import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week05.task04 import solve

class TestTask04(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve({"a": 1, "b": 2}), 3)
        self.assertEqual(solve({}), 0)
