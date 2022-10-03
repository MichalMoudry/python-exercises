"""
Panagram exercise module.
"""

import string

def is_pangram(sentence: str) -> bool:
    sentence = sentence.strip(".").replace(" ", "").lower()
    for letter in string.ascii_lowercase:
        if sentence.find(letter) == -1: return False
    return True