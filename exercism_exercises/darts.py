"""
Darts exercise module.
"""

def score(x: float, y: float) -> int:
    if x < 0: x = -x
    if y < 0: y = -y
    print(x, y)
    return 10

print(score(0.8, -0.8))
