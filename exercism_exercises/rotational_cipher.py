"""
Rotational cipher exercise module.
"""

letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
alphabet = [item for item in enumerate(letters)]
alphabet_length = len(alphabet)
non_alphabet_chars = (" ", ".", ",", "!", "'")

def rotate(text: str, key: int) -> str:
    result = []
    character = ""
    for char in text:
        if not char.isdigit() and char not in non_alphabet_chars:
            character = alphabet[(letters.index(char.lower()) + key) % alphabet_length][1]
            result.append(character.upper() if char.isupper() else character)
        else:
            result.append(char)
    return "".join(result)

print(rotate("a", 0), "- Expected: a")
print(rotate("a", 26), "- Expected: a")
print(rotate("n", 13), "- Expected: a")
print(rotate("O M G", 5), "- Expected: T R L")
print(rotate("OMG", 5), "- Expected: TRL")
print(rotate("Testing 1 2 3 testing", 4), "- Expected: Xiwxmrk 1 2 3 xiwxmrk")
