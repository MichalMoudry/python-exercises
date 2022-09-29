"""
Bob exercise module.
"""

def response(hey_bob: str) -> str:
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob[-1] != "?":
        return "Whoa, chill out!"
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    if hey_bob[-1] == "?":
        return "Sure."
    return "Whatever."

print(response("Okay if like my  spacebar  quite a bit?   "))
