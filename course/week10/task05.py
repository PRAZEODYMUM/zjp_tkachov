"""
Zadanie:
Použi scipy.stats.linregress na lineárny model a vráť (slope, intercept).

Vstup: x, y: zoznamy čísel
Vystup: dvojica (slope, intercept)
Priklad:
Vstup: x=[0,1,2], y=[0,2,4]
Vystup: (2.0, 0.0)
"""

from scipy.stats import linregress

def solve(x, y):
    result=linregress(x,y)
    return (result.slope, result.intercept)