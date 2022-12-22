"""
Transpose exercise module.
"""

def transpose(lines: list[str]):
    result: list[str] = []
    for line in lines:
        print([item for item in enumerate(line)])
        for item in line:
            result.append(item)
    return result

lines = ["ABC", "123"]
#lines = ["Single line."]
expected = ["A1", "B2", "C3"]
result = transpose(lines)

print(result, "=>", expected == result)
