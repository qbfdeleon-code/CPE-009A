def word_filter(sentence, bad_words):
    for word in bad_words:
        censored = "*" * len(word)
        sentence = sentence.replace(word, censored)
    return sentence

print(word_filter("What the fudge", ["fudge"]))

print(word_filter("I hate my pen", ["pen"]))