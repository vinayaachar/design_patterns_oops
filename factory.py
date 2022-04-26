class Dog:
    def __init__(self, name) -> None:
        self._name = name

    def speak(self):
        return 'Woof!'

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns Dog Object"""
        return Dog('seb')

    def get_food(self):
        """Returns Dog food object"""
        return 'Dog Food!'


class PetStore:

    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract factory"""

        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of objects returned"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}!")
        print(f"Our pet says hello by {pet.speak()}")
        print(f"Its food is {pet_food}")


factory = DogFactory()

shop = PetStore(factory)

print(shop.show_pet())
