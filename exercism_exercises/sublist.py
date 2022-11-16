"""
Sublist exercise module.s
"""

# Possible sublist categories.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def is_smaller_list_in_larger_list(smaller_list: list, larger_list: list, small_list_length: int) -> bool:
    for i, _ in enumerate(larger_list):
        if larger_list[i:small_list_length + i] == smaller_list:
            return True
    return False

def sublist(list_one: list, list_two: list) -> str:
    if list_one == list_two: return EQUAL
    list_one_length = len(list_one)
    list_two_length = len(list_two)
    if list_one_length < list_two_length and is_smaller_list_in_larger_list(list_one, list_two, list_one_length):
        return SUBLIST
    elif list_one_length > list_two_length and is_smaller_list_in_larger_list(list_two, list_one, list_two_length):
        return SUPERLIST
    return UNEQUAL

print(sublist([1, 1, 2], [0, 1, 1, 1, 2, 1, 2]), "=> Expected:", SUBLIST)
print(sublist([0, 1, 2], [0, 1, 2, 3, 4, 5]), "=> Expected:", SUBLIST)
print(sublist([1, 2], [1, 22]), "=> Expected:", UNEQUAL)
print(sublist([0, 1, 2, 3, 4, 5], [2, 3]), "=> Expected:", SUPERLIST)
print(sublist([1, 3], [1, 2, 3]), "=> Expected:", UNEQUAL)
