"""
Flatten array exercise module.
"""

def flatten(iterable):
    result = []
    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item != None:
            result.append(item)
    return result

if __name__ == "__main__":
    print("[[[]]] =>", flatten([[[]]]), "(expected: [])", "\n")
    print("[1, [2, 3, 4, 5, 6, 7], 8] =>", flatten([1, [2, 3, 4, 5, 6, 7], 8]), "(expected: [1, 2, 3, 4, 5, 6, 7, 8])", "\n")
    print("[0, 1, 2] =>", flatten([0, 1, 2]), "(expected: [0, 1, 2])", "\n")
    print("[0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2] =>", flatten([0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]), "(expected: [0, 2, 2, 3, 8, 100, 4, 50, -2])", "\n")
    print("[1, 2, None] =>", flatten([1, 2, None]), "(expected: [1, 2])")
