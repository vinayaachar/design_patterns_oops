class Wine():
    def __init__(self) -> None:
        self.country = None
        self.type = None
        self.grape = None

    def __str__(self) -> str:
        return 'This wine is from {} , type is {} and grape varietal is {}'.format(self.country, self.type, self.grape)


class Builder():
    def __init__(self) -> None:
        self.wine = None

    def get_wine(self):
        self.wine = Wine()


class ItalianRed(Builder):
    def __init__(self) -> None:
        Builder.__init__(self)

    def manufacture_wine(self):
        self.wine.country = 'Italy'
        self.wine.type = "Red"
        self.wine.grape = 'Sangiovese'


class Director():
    def __init__(self, builder) -> None:
        self.builder = builder
        self.builder.get_wine()

    def construct_wine(self):
        self.builder.manufacture_wine()

    def get_wine(self):
        return self.builder.wine


w = ItalianRed()
d = Director(w)
d.construct_wine()

print(d.get_wine())
