import pprint

data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = []
for num in data:
    if not num % 2:
        evens.append(num)
pprint.pprint(evens)
print()

data2 = [num for num in data if not num % 2]
pprint.pprint(data2)
print()

data3 = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data3:
    if isinstance(num, str):
        words.append(num)
pprint.pprint(words)
print()

data4 = [num for num in data3 if isinstance(num, str)]
pprint.pprint(data4)
print()

data5 = list('So long and thanks for all the fish'.split())
title = []
for word in data5:
    title.append(word.title())
pprint.pprint(title)
print()

data6 = [word.title() for word in data5]
pprint.pprint(data6)
print()
