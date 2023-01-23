"""
Matching brackets exercise module.
"""

PAIRS = {
    "(": ")",
    ")": "(",
    "{": "}",
    "[": "]"
}

def is_paired(input_string: str) -> bool:
    unique_chars = list(set(input_string))
    result = False
    for char in unique_chars:
        if char == "[":
            print(char, PAIRS[char], PAIRS[char] in unique_chars)
        elif char == "{":
            print(char, PAIRS[char], PAIRS[char] in unique_chars)
        elif char == "(" or char == ")":
            print(char, PAIRS[char], PAIRS[char] in unique_chars)
    return result

if __name__ == "__main__":
    print(is_paired("([[]]{}"), "Expected: True")
    print(is_paired("{[)][]}"), "Expected: False")
