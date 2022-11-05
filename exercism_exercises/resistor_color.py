"""
Resistor color exercise module.
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

def color_code(color: str) -> int:
    return COLOR_CODES.pop(color)

def colors() -> list[str]:
    return list(COLOR_CODES.keys())

print(colors())
print(color_code("white"))
