"""
Pig latin exercise module.
"""

VOWELS = ("a", "e", "i", "o", "u")
CONSONANTS = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")

def translate(text: str) -> str:
    lower_text = text.lower()
    result: list[str] = []
    consonants: list[str] = []
    text_length = len(text)
    first_letter = lower_text[0]
    first_two_letters = lower_text[0:2]
    for i, char in enumerate(text):
        if i < text_length - 1 and lower_text[i + 1] in CONSONANTS:
            consonants.append(char)
            consonants.append(text[i + 1])
        else: break
    consonant_cluster = "".join(consonants)
        
    if first_letter in VOWELS or (first_two_letters == "xt" or first_two_letters == "yt"): # rule 1
        result.append(text)
    elif first_letter in CONSONANTS: # rule 2
        result.append(text[len(consonants):])
        result.append(consonant_cluster)
    """
    if first_letter in VOWELS or first_two_letters in VOWELS:
        result.append(text)
    elif first_letter in CONSONANTS and second_and_third_letter != "qu":
        result.append(text[1:])
        result.append(text[0])
    elif first_letter in CONSONANTS and second_and_third_letter == "qu":
        result.append(text[3:])
        result.append(text[0])
        result.append(second_and_third_letter)
    """
    result.append("ay")
    return "".join(result)

print(translate("chair"))
