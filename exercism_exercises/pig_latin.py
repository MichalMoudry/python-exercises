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
    # TODO: Find consonant cluster

    """if first_letter in VOWELS or (first_two_letters == "xr" or first_two_letters == "yt"): # rule 1
        result.append(text)
    elif text.startswith(consonant_cluster) and consonant_cluster_with_qu == -1 and consonant_cluster_with_y == -1: # rule 2
        result.append(text[cluster_length:])
        result.append(consonant_cluster)
    elif text.startswith(consonant_cluster) and consonant_cluster_with_qu != -1: # rule 3
        result.append(text[cluster_length + 1:])
        result.append(text[:cluster_length + 1])
    elif consonant_cluster_with_y != -1: # rule 4
        result.append(text[cluster_length:])
        result.append(text[:cluster_length])
        result.append("-")"""
    result.append("ay")
    return "".join(result)

print(translate("rhythm"))
