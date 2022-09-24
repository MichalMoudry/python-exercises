"""
Armstrong number exercise module.
"""

def is_armstrong_number(number: int) -> bool:
    string_number = str(number)
    number_length = len(string_number)
    total = 0
    for char in string_number:
        total += pow(int(char), number_length)
    return number == total

print(is_armstrong_number(153))