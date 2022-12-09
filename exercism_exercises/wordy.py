"""
Wordy exercise module.
"""

def answer(question: str):
    input = question
    if not input.startswith("What is ") or not input.endswith("?"):
        raise ValueError("syntax error")
    input = input.removeprefix("What is ").removesuffix("?")
    print(f"'{input}'")
    input_length = len(input)
    if input_length == 1: return int(input)
    items = enumerate(input.split(" "))
    print([item for item in items])
    return 0

print(answer("What is 5 plus 5 plus 7?"))
