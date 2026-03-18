import os
import sys
import unittest
import numpy as np
from numpy.testing import assert_array_equal

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week10.task02 import solve

class TestTask02(unittest.TestCase):
    def test_main(self):
        result = solve([[1, 2], [3, 4]])
        self.assertIsInstance(result, np.ndarray)
        assert_array_equal(result, np.array([[1, 3], [2, 4]]))
