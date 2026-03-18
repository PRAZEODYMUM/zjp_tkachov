import os
import sys
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week10.task04 import solve

class TestTask04(unittest.TestCase):
    def test_main(self):
        values = [1, 5, 2, 8]
        result = solve(values, 4)
        self.assertIsInstance(result, pd.DataFrame)
        expected = pd.DataFrame({"v": [5, 8]})
        result = result.reset_index(drop=True)
        expected = expected.reset_index(drop=True)
        assert_frame_equal(result, expected)
