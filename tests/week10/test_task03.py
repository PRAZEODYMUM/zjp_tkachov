import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week10.task03 import solve

class TestTask03(unittest.TestCase):
    def test_main(self):
        data = {"a": [1, 2, 3], "b": [10, 20, 30]}
        self.assertEqual(solve(data), 6)
