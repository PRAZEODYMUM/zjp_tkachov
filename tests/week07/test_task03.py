import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week07.task03 import Rectangle

class TestTask03(unittest.TestCase):
    def test_main(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)
        self.assertEqual(r.perimeter(), 14)
