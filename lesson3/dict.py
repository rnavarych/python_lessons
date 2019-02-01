vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Type please:')
found = {}

# for vowel in vowels:
#     found[vowel] = 0

# for symbol in word:
#     if symbol in vowels:
#         if symbol in found:
#             found[symbol] += 1
#         else:
#             found[symbol] = 1

for symbol in word:
    if symbol in vowels:
        found.setdefault(symbol, 0)
        found[symbol] += 1

for k, v in sorted(found.items()):
    print('key: ', k, ' - value: ', v)
