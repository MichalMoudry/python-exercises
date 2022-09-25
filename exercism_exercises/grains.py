"""
Grains exercise module.
"""

def square(number):
    if number <= 0 or number > 64: raise ValueError("square must be between 1 and 64")
    previous = 1
    for square_number in range(1, number + 1):
        previous -= 1
        if square_number == number:
            return 2 ** (-previous)


def total():
    sm = 0
    for i in range(1, 65):
        sm += square(i)
    return sm


print(square(32))
print(total())