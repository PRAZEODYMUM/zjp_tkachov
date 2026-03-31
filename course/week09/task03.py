"""
Zadanie:
Vytvor bodový graf, nastav názov a vráť objekt Figure.

Vstup: x, y: zoznamy čísel, title: reťazec
Vystup: matplotlib.figure.Figure
Priklad:
Vstup: x=[1,2], y=[3,4], title="Body"
Vystup: Figure
"""

import matplotlib.pyplot as plt

def solve(x, y, title):
    fig, ax=plt.subplots()
    ax.scatter(x,y)
    ax.set_title(title)
    return fig