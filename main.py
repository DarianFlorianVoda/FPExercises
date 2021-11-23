#Assignment 1
file = open("sherlock.txt")
data = file.readlines()
file.close()
collection = {
    '!': 's',
    '@': 'h',
    '#': 'e',
    '$': 'r',
    '%': 'l',
    '^': 'o',
    '&': 'c',
    '*': 'k'
}

#Exercise 1
def fun(l):
    for i in l:
        if i in collection:
            return collection[i]
        else:
            return i

l = []
alist = []
print("Exercise 1: ")
for i in data:
    y = i.split()
    word = map(lambda w: "".join(map(fun, w)), y)
    l = " ".join(word)
    print(l)
    a = filter(lambda x: x.startswith("a"), l.split())
    alist.extend(a)

#Exercise 2&3&4
print(alist)
