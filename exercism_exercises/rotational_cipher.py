"""
Rotational cipher exercise module.
"""

alphabet = {
    "a": 1,
    "b": 2,
}

def rotate(text: str, key: int) -> str:
    lower_text = text.lower()
    chars = lower_text.split(" ")
    print(chars)
    return ""

print(rotate("a", 0), " - Expected: a")
print(rotate("a", 26), " - Expected: a")
print(rotate("n", 13), " - Expected: a")
