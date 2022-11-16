"""
All your base exercise module.
"""

def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2: raise ValueError("input base must be >= 2")
    elif output_base < 2: raise ValueError("output base must be >= 2")
    input_number = 0
    try:
        input_number = int(str(digits).replace(", ", "").removeprefix("[").removesuffix("]"))
    except ValueError:
        raise ValueError("TEst")
    print(input_number)
    res: list[int] = []
    for i, number in enumerate(digits):
        print("index ->", i, "| number ->", number)
    return res

rebase(2, [1, 0, -1], 10)
