"""
Wordy exercise module.
"""

def answer(question: str):
    input = question
    if not input.startswith("What is ") or not input.endswith("?"):
        raise ValueError("syntax error")
    input = input.removeprefix("What is ").removesuffix("?")
    print(f"'{input}'")
    pass

answer("What is 5 plus -5?")
