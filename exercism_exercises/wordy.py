"""
Wordy exercise module.
"""

def answer(question: str):
    inpt = question
    if inpt.startswith("Who"): raise ValueError("unknown operation")
    elif not inpt.startswith("What is ") or not inpt.endswith("?"): raise ValueError("syntax error")
    result = 0
    inpt = inpt.removeprefix("What is ").removesuffix("?").replace(" by", "by")
    items = inpt.split(" ")
    lenght = len(items)
    if lenght == 1: return int(inpt)
    elif lenght == 2:
        if inpt.endswith("plus"): raise ValueError("syntax error")
        raise ValueError("unknown operation")
    try:
        for tup in enumerate(items):
            if tup[0] == 0: result = int(tup[1])
            elif tup[0] % 2 != 0:
                if tup[1] == "multipliedby":
                    result = result * int(items[tup[0] + 1])
                elif tup[1] == "plus":
                    result = result + int(items[tup[0] + 1])
                elif tup[1] == "minus":
                    result = result - int(items[tup[0] + 1])
                else:
                    result = result // int(items[tup[0] + 1])
    except:
        raise ValueError("syntax error")
    return result

print(answer("Who is the President of the United States?"))
