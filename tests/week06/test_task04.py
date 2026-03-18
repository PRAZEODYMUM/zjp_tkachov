import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week06.task04 import solve

class TestTask04(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve(2), 9)
        self.assertEqual(solve(-1), 0)
