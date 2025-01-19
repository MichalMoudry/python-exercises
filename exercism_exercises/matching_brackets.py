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
    if input_string == "" or len(input_string) % 2 != 0:
        return False

    try:
        for i, char in enumerate(input_string):
            #closest_pair_index = input_string[i+1:].index(PAIRS[char])
            str_evaluation_part = input_string[i+1:]
            if len(str_evaluation_part) == 0:
                break
            print(i, char, "=>", str_evaluation_part)
            #print("Closest pair index:", closest_pair_index)
    except:
        return False
    return False

print("Is [] paired?", is_paired("[]"))
print(4 * "---")

print("Is '' paired?", is_paired(""))
print(4 * "---")

print("Is [[ paired?", is_paired("[["))
print(4 * "---")

print("Is {}[] paired?", is_paired("{}[]"))

