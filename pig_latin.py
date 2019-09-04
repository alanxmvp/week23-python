from arepl_dump import dump

vowels = ["a", "e", "i", "o", "u"]

def convert(word):
    firstVowelIdx = None

    for idx, char in enumerate(word):
        if char in vowels:
            firstVowelIdx = idx
            break

    if firstVowelIdx == 0:
        return word
    elif firstVowelIdx != None and firstVowelIdx > 0:
        return word[firstVowelIdx : len(word)] + word[0:firstVowelIdx] + "ay"
    else:
        return word + "ay"
 
print(convert("art") == ("art"))
print(convert("vowel") == ("owelvay"))
print(convert("nginx") == ("inxngay"))
print(convert("hello") == ("ellohay"))
print(convert("Dr") == ("Dray"))