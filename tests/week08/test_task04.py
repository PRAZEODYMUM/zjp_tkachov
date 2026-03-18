import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week08.task04 import is_palindrome

class TestTask04(unittest.TestCase):
    def test_main(self):
        self.assertTrue(is_palindrome("Kobyla ma maly bok"))
        self.assertFalse(is_palindrome("Python"))
