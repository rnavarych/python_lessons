from countfromby import CountFromBy

a = CountFromBy(100, 10)
j = CountFromBy(100, 10)
print(a.val)
print('----------------------------')

a.increase()
print(a.val)
print('----------------------------')

print(type(j))
print(id(j))
print(hex(id(j)))
