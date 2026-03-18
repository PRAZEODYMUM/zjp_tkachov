import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week08.task03 import prefix_text

class TestTask03(unittest.TestCase):
    def test_main(self):
        @prefix_text("Ahoj ")
        def meno(m):
            return m

        self.assertEqual(meno("Eva"), "Ahoj Eva")
