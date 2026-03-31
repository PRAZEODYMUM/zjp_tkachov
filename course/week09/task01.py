"""
Zadanie:
Vytvor čiarový graf z hodnôt x a y, nastav názov grafu a vráť objekt Figure.

Vstup: x, y: zoznamy čísel, title: reťazec
Vystup: matplotlib.figure.Figure
Priklad:
Vstup: x=[0,1], y=[1,2], title="Test"
Vystup: Figure
"""

import matplotlib.pyplot as plt

def solve(x, y, title):
    fig, ax=plt.subplots()
    ax.plot(x,y)
    ax.set_title(title)
    return fig