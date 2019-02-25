msg = "My string"


def hello():
    print(msg)


print(id(hello))
print(type(msg))
print(type(hello))


def outer():
    def inner():
        print('Inner function')

    print('Outer function')
    return inner


i = outer()
print(i)
print(type(i))
i()
print('---------------------------------')


def custom(*args):
    for i in args:
        print(i, end=' ')
    if args:
        print()


custom(1, 2, 'q', 5, 'q')


def custom2(**kargs):
    for k,v in kargs.items():
        print(k, v, sep='->', end=' ')
    if kargs:
        print()


custom2(a=10, b=20)


def custom3(*args, **kwargs):
    for i in args:
        print(i, end=' ')
    print()
    if kwargs:
        for k,v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


custom3(1, 2, 3, a=23, b=44, c=55)
