"""
Isogram exercise module.
"""

def is_isogram(string: str) -> bool:
    string = string.lower().replace("-", "").replace(" ", "")
    for char in enumerate(string):
        if char[0] != string.index(char[1]):
            return False
    return True

print(is_isogram("Alphabet"), "- Expected: False")
print(is_isogram("abc-def-"), "- Expected: True")
print(is_isogram("isograms"), "- Expected: False")
