"""
Sublist exercise module.s
"""

# Possible sublist categories.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def is_smaller_list_in_larger_list(smaller_list: list, larger_list: list) -> bool:
    print(set(larger_list), set(smaller_list))
    return True

def sublist(list_one: list, list_two: list) -> str:
    if list_one == list_two: return EQUAL
    list_one_length = len(list_one)
    list_two_length = len(list_two)
    if list_one_length < list_two_length and is_smaller_list_in_larger_list(list_one, list_two):
        return SUBLIST
    elif list_one_length > list_two_length and is_smaller_list_in_larger_list(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

test1 = ["A", "B", "C", "D"]
test2 = ["A", "B"]

"""print(sublist(test1, test2))
print(sublist([1, 2], [1, 2, 3]))
print(sublist([1, 3], [1, 2, 3]))"""
print(sublist([1, 1, 2], [0, 1, 1, 1, 2, 1, 2]))
