class Parent():
    def __init__(self, wife) -> None:
        self.wife = wife

    def __str__(self) -> str:
        return 'testing'


class Child(Parent):
    def __init__(self, wife, dad) -> None:
        self.dad = dad
        Parent.__init__(self, wife)

    def get_parent(self):
        return 'My mother is {} and father is {}'.format(self.wife, self.dad)


child = Child('Anna', 'Vinay')

# print(child.get_parent())


# test args and kwargs

def argsKwargs(*args, **kwargs):
    for num in args:
        print(num)

    for key, val in kwargs.items():
        print(key, val)


print(argsKwargs(1, 2, 3, first='vinay', last='rao'))
