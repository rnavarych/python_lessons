def check_annotations(code: str) -> str:
    return code


out = check_annotations('text')
print(out)


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Возвращает множество букв из letters"""
    return set(letters).intersection(phrase)


print(search4letters('Ahaha... where?'))
print(search4letters(letters='aeou', phrase='Ahaha... where?'))



