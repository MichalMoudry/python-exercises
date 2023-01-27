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
    unique_chars = set([char for char in input_string if char in PAIRS.keys()])
    eval_result = False
    for char in enumerate(unique_chars):
        #eval_result = PAIRS[char] not in unique_chars
        """if char == "[" and eval_result:
            return False
        elif char == "{" and eval_result:
            return False
        elif char == "(" and eval_result:
            return False
        elif char == "]" and eval_result:
            return False
        elif char == ")" and eval_result:
            return False"""
        print(f"{char} => {eval_result}")
    return True

if __name__ == "__main__":
    #print(is_paired("[[]]{}"), "Expected: True")
    #print(is_paired("{[)][]}"), "Expected: False")
    print(is_paired("}{"), "Expected: False")
