"""
Darts exercise module.
"""

def score(x: float, y: float) -> int:
    x2, y2 = pow(x, 2), pow(y, 2)
    a2 = x2 + y2
    if a2 <= 1:
        return 10
    if a2 <= 25:
        return 5
    if a2 <= 100:
        return 1
    return 0

print(score(-9, 9), "=> Expected:", 0)
