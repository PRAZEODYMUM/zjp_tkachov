"""
Zadanie:
Vytvor stĺpcový graf, nastav názov a vráť objekt Figure.

Vstup: labels: zoznam reťazcov, values: zoznam čísel, title: reťazec
Vystup: matplotlib.figure.Figure
Priklad:
Vstup: labels=["A"], values=[3], title="Stlpce"
Vystup: Figure
"""

import matplotlib.pyplot as plt

def solve(labels, values, title):
    fig, ax=plt.subplots()
    ax.bar(labels,values)
    ax.set_title(title)
    return fig