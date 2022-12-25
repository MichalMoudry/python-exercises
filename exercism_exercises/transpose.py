"""
Transpose exercise module.
"""

def transpose(lines: list[str]):
    result: list[str] = []
    column_length = len(lines)
    number_of_rows = 0
    row_length = 0
    for row in lines:
        row_length = len(row)
        if row_length > number_of_rows: number_of_rows = row_length
    print("column length:", column_length, "row length:", row_length)
    for row_index in range(number_of_rows):
        print(f"{row_index}" * column_length)
    return result

lines = ["ABC", "123"]
#lines = ["Single line."]
expected = ["A1", "B2", "C3"]
result = transpose(lines)

print(result, "=>", expected == result)
