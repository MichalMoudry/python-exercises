"""
Perfect numbers exercise module.
"""

def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number == 0: raise ValueError("Classification is only possible for positive integers.")
    elif number < 0: raise ValueError("Classification is only possible for positive integers.")
    numbers_sum = 0
    for i in range(1, number):
        if number % i == 0:
            numbers_sum += i
    if numbers_sum == number:
        return "perfect"
    if numbers_sum > number:
        return "abundant"
    return "deficient"

print(classify(28))
