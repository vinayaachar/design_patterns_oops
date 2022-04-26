class Kannada:
    """Kannada speaker"""

    def __init__(self) -> None:
        self.name = 'Kannada'

    def speak_kannada(self):
        return 'Namaskara'


class British:
    """English speaker"""

    def __init__(self) -> None:
        self.name = 'British'

    def speak_english(self):
        return 'Hello!'


class Adapter:

    def __init__(self, object, **adapted_method) -> None:
        """Change the name of the method"""
        self._object = object

        # A new dict item to establish mapping between different speak methods

        self.__dict__.update(adapted_method)

    def __getattr__(self, attr: str) -> None:
        return getattr(self._object, attr)


# List to store objects

objects = []

# create kannada object
kannada = Kannada()

british = British()

objects.append(Adapter(kannada, speak=kannada.speak_kannada))
objects.append(Adapter(british, speak=british.speak_english))


for obj in objects:
    print(f"{obj.name} says {obj.speak()}")
