import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week08.task01 import assert_positive

class TestTask01(unittest.TestCase):
    def test_main(self):
        self.assertEqual(assert_positive(3), 3)
        with self.assertRaises(ValueError):
            assert_positive(0)
        with self.assertRaises(ValueError):
            assert_positive(-1)
