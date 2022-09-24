"""
Leap year exercise module.
"""

def leap_year(year: int) -> bool:
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return True
    return False

print(leap_year(1997))
print(leap_year(1996))