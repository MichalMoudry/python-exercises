"""
Atbash cipher exercise module.
"""

ALPHABET = [chr(num) for num in range(97, 123)]

def convert_string(string: str) -> str:
    ciphered_text = string.replace(" ", "").lower().removesuffix(".")
    result: list[str] = []
    index = 0
    for char in ciphered_text:
        if char.isalpha():
            index = ALPHABET.index(char)
            result.append(ALPHABET[-1 - index])
        else:
            result.append(char)
    return "".join(result)

def encode(plain_text: str):
    return decode(plain_text)

def decode(ciphered_text: str) -> str:
    ciphered_text = ciphered_text.replace(" ", "").lower().removesuffix(".")
    result: list[str] = []
    index = 0
    for char in ciphered_text:
        if char.isalpha():
            index = ALPHABET.index(char)
            result.append(ALPHABET[-1 - index])
        else:
            result.append(char)
    return "".join(result)

print(encode("mindblowingly"))
