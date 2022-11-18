"""
Resistor color duo exercise module.
"""

COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def value(colors: list[str]) -> int:
    valid_colors = colors[:2]
    return (COLOR_CODES[valid_colors[0]] * 10) + COLOR_CODES[valid_colors[1]]

print(value(["orange", "orange"]))
print(value(["green", "brown", "orange"]))
