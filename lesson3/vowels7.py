vowels = set('aeoui')
word = input("Where are my letters?:")

unique_words = set(vowels).intersection(set(word))

print(unique_words)


