# Assignment 2
from itertools import permutations


# Subpoints a) and b)
def convertTuple(tup):
    # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str


word = input()
result = permutations(word)
anagrams = []
x = map(lambda x: convertTuple(x), result)
anagrams.extend(x)
print(anagrams)

# Subpoint c)
with open("dictionary.txt") as f:
    text = f.read().split("\n")
print(list(filter(lambda x: x in anagrams, text)))

