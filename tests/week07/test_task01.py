import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week07.task01 import Student

class TestTask01(unittest.TestCase):
    def test_main(self):
        s = Student("Eva", 75)
        self.assertTrue(s.passed())
        self.assertTrue(s.passed(70))
        self.assertFalse(s.passed(80))
