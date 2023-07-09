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

"""def is_paired(input_string: str) -> bool:
    input_string = input_string.replace(" ", "")
    print(input_string, "-"*20, sep="\n")
    for char in input_string:
        print(char)
    return False

if __name__ == "__main__":
    #print(is_paired("[[]]{}"), "Expected: True")
    #print(is_paired("{[)][]}"), "Expected: False")
    print(is_paired("{ { } }"))
    #print(is_paired("}{"), "Expected: False")"""

def is_paired(input_string: str) -> bool:
    if len(input_string) % 2 != 0:
        return False
    
    input_list: list[str] = []
    for i, char in enumerate(input_string):
        print(i, "=>", char, PAIRS[char], input_string.index(PAIRS[char]))
    return True

print(is_paired("([{}({}[])])"), "|", "TRUE")
#print(is_paired("}{"), "|", "FALSE")
#print(is_paired("[[]]{}"), "|", "TRUE")
