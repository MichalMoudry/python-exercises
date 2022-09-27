"""
Raindrops exercise module.
"""

def convert(number: int) -> str:
    string = []
    if number % 3 == 0:
        string.append("Pling")
    if number % 5 == 0:
        string.append("Plang")
    if number % 7 == 0:
        string.append("Plong")
    if len(string) == 0:
        return str(number)
    return "".join(string)

print(convert(1))