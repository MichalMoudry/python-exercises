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
    value_comparison = [(item in list_one) for item in list_two]
    print(list_two, value_comparison)
    if list_two in list_one:
        return SUPERLIST
    return SUBLIST

test1 = ["A", "B", "C"]
test2 = ["A", "B"]

print(sublist(test1, test2))
