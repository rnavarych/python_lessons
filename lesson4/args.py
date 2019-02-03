num = 10


def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


double(num)
print(num)


val = [42, 46, 13]


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


change(val)
print(val)
