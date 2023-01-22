"""
Matching brackets exercise module.
"""

def is_paired(input_string: str) -> bool:
    unique_chars = set(input_string)
    return True

if __name__ == "__main__":
    print(is_paired("[[]]"), "Expected: True")
    print(is_paired("[["), "Expected: False")
