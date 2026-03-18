import os
import sys
import unittest
import matplotlib
matplotlib.use("Agg")
from matplotlib.figure import Figure

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week09.task03 import solve

class TestTask03(unittest.TestCase):
    def test_main(self):
        x = [1, 2]
        y = [3, 4]
        fig = solve(x, y, "Body")
        self.assertIsInstance(fig, Figure)
        ax = fig.axes[0]
        self.assertEqual(len(ax.collections), 1)
        offsets = ax.collections[0].get_offsets()
        self.assertEqual(len(offsets), 2)
        self.assertEqual([float(v) for v in offsets[:, 0]], x)
        self.assertEqual([float(v) for v in offsets[:, 1]], y)
        self.assertEqual(ax.get_title(), "Body")
