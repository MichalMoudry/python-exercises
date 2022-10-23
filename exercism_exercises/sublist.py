"""
Sublist exercise module.s
"""

# Possible sublist categories.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def eval_superlist(list_one: list, list_two: list) -> str:
    for item in enumerate(list_two):
        if item[1] != list_one[item[0]]:
            return UNEQUAL
    return SUPERLIST

def eval_sublist(list_one: list, list_two: list) -> str:
    return SUBLIST

def sublist(list_one: list, list_two: list) -> str:
    if list_one == list_two:
        return EQUAL
    try:
        result = eval_superlist(list_one, list_two)
        if result == SUPERLIST:
            return SUPERLIST
    except:
        result = eval_sublist(list_one, list_two)
        if result == SUBLIST:
            return SUBLIST
        return UNEQUAL
    return UNEQUAL

test1 = ["A", "B", "C", "D"]
test2 = ["A", "B"]

print(sublist(test2, test1))
#print(sublist([1, 2], [1, 2, 3]))
