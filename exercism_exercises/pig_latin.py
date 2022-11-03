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
        consonants.append(char)
        if i < text_length - 1 and lower_text[i + 1] in CONSONANTS: continue
        else: break
    consonant_cluster = "".join(consonants)
    cluster_length = len(consonant_cluster)
    consonant_cluster_with_qu = text.find(consonant_cluster + "u")
    consonant_cluster_with_y = text.find(consonant_cluster + "y")
    
    if first_letter in VOWELS or (first_two_letters == "xr" or first_two_letters == "yt"): # rule 1
        result.append(text)
    elif text.startswith(consonant_cluster) and consonant_cluster_with_qu == -1 and consonant_cluster_with_y == -1: # rule 2
        result.append(text[cluster_length:])
        result.append(consonant_cluster)
    elif text.startswith(consonant_cluster) and consonant_cluster_with_qu != -1: # rule 3
        result.append(text[cluster_length + 1:])
        result.append(text[:cluster_length + 1])
    result.append("ay")
    return "".join(result)

print(translate("rhythm"))
