vowels3 = {}
vowels3['a'] = 0
vowels3['e'] = 0
vowels3['i'] = 0
vowels3['o'] = 0
vowels3['u'] = 0

print(vowels3)

vowels3['e'] += 1

print(vowels3)

for key in vowels3:
    print("key: ", key, " - value: ", vowels3[key])

print()

for key in sorted(vowels3):
    print("key: ", key, " - value: ", vowels3[key])

print()

for k,v in sorted(vowels3.items()):
    print("key: ", k, " - value: ", v)
