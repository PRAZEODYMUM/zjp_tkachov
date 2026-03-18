import os
import sys
import unittest
import matplotlib
matplotlib.use("Agg")
from matplotlib.figure import Figure

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week09.task01 import solve

class TestTask01(unittest.TestCase):
    def test_main(self):
        x = [0, 1, 2]
        y = [0, 1, 4]
        fig = solve(x, y, "Test")
        self.assertIsInstance(fig, Figure)
        self.assertEqual(len(fig.axes), 1)
        ax = fig.axes[0]
        self.assertEqual(len(ax.lines), 1)
        line = ax.lines[0]
        self.assertEqual(list(line.get_xdata()), x)
        self.assertEqual(list(line.get_ydata()), y)
        self.assertEqual(ax.get_title(), "Test")
