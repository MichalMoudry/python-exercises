"""
Atbash cipher exercise module.
"""

ALPHABET = [chr(num) for num in range(97, 123)]

def convert_string(string: str) -> str:
    ciphered_text = string.replace(" ", "").replace(",", "").lower().removesuffix(".")
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
    cipher_text = convert_string(plain_text)
    result: list[str] = []
    for index, char in enumerate(cipher_text):
        result.append(char)
        if (index + 1) % 5 == 0: result.append(" ")
    return ("".join(result)).strip()

def decode(ciphered_text: str) -> str:
    return convert_string(ciphered_text)

print(encode("mindblowingly"))
print(decode("vcvix rhn"))
