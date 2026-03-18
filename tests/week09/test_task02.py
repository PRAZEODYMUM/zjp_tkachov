import os
import sys
import unittest
import matplotlib
matplotlib.use("Agg")
from matplotlib.figure import Figure

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week09.task02 import solve

class TestTask02(unittest.TestCase):
    def test_main(self):
        labels = ["A", "B", "C"]
        values = [3, 5, 2]
        fig = solve(labels, values, "Stlpce")
        self.assertIsInstance(fig, Figure)
        ax = fig.axes[0]
        self.assertEqual(len(ax.patches), 3)
        heights = [p.get_height() for p in ax.patches]
        self.assertEqual(heights, values)
        self.assertEqual(ax.get_title(), "Stlpce")
