"""
Secret handshake exercise module.
"""

COMMANDS = {
    "0": "jump",
    "1": "close your eyes",
    "2": "double blink",
    "3": "wink"
}

def commands(binary_str: str):
    input = [char for char in binary_str[1:]]
    res: list[str] = []
    for i, char in enumerate(input):
        if char == "1":
            res.append(COMMANDS[f"{i}"])
    if binary_str[0] == "0": res.reverse()
    return res

print(commands("10011"))
print(commands("11000"))
print(commands("00011"))