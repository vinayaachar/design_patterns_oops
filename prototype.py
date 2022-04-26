import copy


class Prototype:

    def __init__(self) -> None:
        self._objects = {}

    def register_obects(self, name: str, obj: dict) -> None:
        """Register an object"""
        self._objects[name] = obj

    def unregistered_object(self, name: str) -> None:
        """Unregister an Object"""

        del self._objects[name]

    def clone(self, name: str, **attr) -> dict:
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self) -> None:
        self.name = 'Skylark'
        self.color = 'Red'
        self.options = 'Ex'

    def __str__(self) -> str:
        return '{} | {} | {}'.format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_obects('skylark', c)

c1 = prototype.clone('skylark')

print(c1)
