"""
Matching brackets exercise module.
"""

PAIRS = {
    "(": ")",
    ")": "(",
    "{": "}",
    "}": "{",
    "[": "]",
    "]": "["
}

def is_paired(input_string: str) -> bool:
    unique_chars = list(set(input_string))
    eval_result = False
    for char in unique_chars:
        eval_result = PAIRS[char] not in unique_chars
        if char == "[" and eval_result:
            return False
        elif char == "{" and eval_result:
            return False
        elif char == "(" and eval_result:
            return False
        elif char == "]" and eval_result:
            return False
        elif char == ")" and eval_result:
            return False
    return True

if __name__ == "__main__":
    print(is_paired("[[]]{}"), "Expected: True")
    print(is_paired("{[)][]}"), "Expected: False")
