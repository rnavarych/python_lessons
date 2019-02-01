from pprint import pprint

first = {'gender': 'male', 'firstName': "Yan", 'secondName': "Syrokvash", 'age': 28}
second = {'gender': 'female', 'firstName': "Olya", 'secondName': "Who", 'age': 29}
third = {'gender': 'male', 'firstName': "Paul", 'secondName': "Cool", 'age': 14}
fourth = {'gender': 'male', 'firstName': "Ben", 'secondName': "Yandex", 'age': 68}

people = {}
people['Yan'] = first
people['Olya'] = second
people['Paul'] = third
people['Ben'] = fourth

print(people)
print()
pprint(people)
print(people['Yan']['age'])
