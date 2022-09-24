"""
Difference of squares exercise module.
"""

def square_of_sum(number: int) -> int:
    number_list = [x for x in range(1, number + 1)]
    return sum(number_list) ** 2

def sum_of_squares(number: int) -> int:
    mapped_list = [x ** 2 for x in range(1, number + 1)]
    return sum(mapped_list)

def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)