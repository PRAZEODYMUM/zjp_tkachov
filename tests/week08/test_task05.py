import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week08.task05 import safe_divide

class TestTask05(unittest.TestCase):
    def test_main(self):
        self.assertEqual(safe_divide(10, 2), 5)
        self.assertIsNone(safe_divide(5, 0))
