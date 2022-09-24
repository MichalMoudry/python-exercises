"""
Triangle exercise module.
"""

def zero_length_check(sides) -> bool:
    for side in sides:
        if side == 0: return False
    return True

def is_triangle_inequal(sides) -> bool:
    a, b, c = sides[0], sides[1], sides[2]
    if a + b < c or a + c < b or b + c < a:
        return True
    return False

def equilateral(sides):
    if not zero_length_check(sides) or is_triangle_inequal(sides):
        return False
    return sides[0] == sides[1] == sides[2]

def isosceles(sides):
    if not zero_length_check(sides) or is_triangle_inequal(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]

def scalene(sides) -> bool:
    if not zero_length_check(sides) or is_triangle_inequal(sides):
        return False
    return not isosceles(sides)