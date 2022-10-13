"""
ISBN verifier exercise module.
"""

def is_valid(isbn: str) -> bool:
    """
    Function for validating a ISBN-10 string.
    """
    isbn = isbn.replace("-", "")
    index = len(isbn)
    if index != 10: return False
    val = total = 0
    for char in isbn:
        if char == "X" and index == 1: char = "10"
        try:
            val = int(char)
            total += val * index
            print(index, val, "=>", total)
        except ValueError:
            return False
        index -= 1
    return total % 11 == 0

print(is_valid("98245726788"))
