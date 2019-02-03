def search_vowels(word):
    """Print symbols"""
    vowels = set('aeoui')
    unique_words = set(vowels).intersection(set(word))

    print(unique_words)
    return sorted(vowels)


v2 = search_vowels('wtf oooooh ne ia')
print()
print(bool(v2))
print(v2)
