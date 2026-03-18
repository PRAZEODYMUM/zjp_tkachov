import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week07.task02 import Counter

class TestTask02(unittest.TestCase):
    def test_main(self):
        c = Counter()
        self.assertEqual(c.value(), 0)
        self.assertEqual(c.inc(), 1)
        self.assertEqual(c.inc(), 2)
        self.assertEqual(c.dec(), 1)
        self.assertEqual(c.value(), 1)
        c2 = Counter(5)
        self.assertEqual(c2.value(), 5)
