import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week08.task02 import double_result

class TestTask02(unittest.TestCase):
    def test_main(self):
        @double_result
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 10)
