"""
Sublist exercise module.s
"""

# Possible sublist categories.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def sublist(list_one: list, list_two: list) -> str:
    if list_one == list_two:
        return EQUAL
    try:
        test = [list_two.index(item) for item in list_one]
        print(test)
    except ValueError:
        return UNEQUAL
    return UNEQUAL

test1 = ["A", "B", "C"]
test2 = ["A", "B", "C"]

#print(sublist(test1, test2))
print(sublist([1, 2], [1, 2, 3]))
