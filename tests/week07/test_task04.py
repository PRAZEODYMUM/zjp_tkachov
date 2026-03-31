import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week07.task04 import Dog, Animal

class TestTask04(unittest.TestCase):
    def test_main(self):
        a = Animal()
        d = Dog()
        self.assertEqual(a.sound(), "ticho")
        self.assertEqual(d.sound(), "haf")
