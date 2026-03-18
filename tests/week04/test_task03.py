import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week04.task03 import solve

class TestTask03(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve([1, 2, 1, 3, 2]), [1, 2, 3])
        self.assertEqual(solve(["a", "a", "b"]), ["a", "b"])
