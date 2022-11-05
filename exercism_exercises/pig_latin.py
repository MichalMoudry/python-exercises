"""
Pig latin exercise module.
"""

def translate_word(word):
    while not word[0] in 'aeiou':
        if word[0] in 'xy' and not word[1] in 'aeiou':
            break
        word = word[1:] + word[0]
        if word[-1] == 'q' and word[0] == 'u':
            word = word[1:] + 'u'
    return word + 'ay'

def translate(sentence):
    return ' '.join([translate_word(word) for word in sentence.split()])

print(translate("xray"), "=> Expected: xrayay")
print(translate("chair"), "=> Expected: airchay")
print(translate("square"), "=> Expected: aresquay")
print(translate("rhythm"), "=> Expected: ythmrhay")
print(translate("my"), "=> Expected: ymay")
