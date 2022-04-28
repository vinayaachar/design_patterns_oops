class Component(object):
    """Abstarct class"""

    def __init__(self, *args, **kwargs) -> None:
        pass

    def component_function(self):
        pass


class Child(Component):
    """Concrete class"""

    def __init__(self, *args, **kwargs) -> None:
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print('{}'.format(self.name))


class Composite(Component):

    def __init__(self, *args, **kwargs) -> None:
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print(f"{self.name}")

        for i in self.children:
            i.component_function()


# Build a composite sub menu 1
sub1 = Composite("submenu1")


# Create a new child sub_menu 11
sub11 = Child("sub_submenu 11")
# Create a new Child sub_submenu
sub12 = Child("sub_submenu 12")


sub1.append_child(sub11)
sub1.append_child(sub12)

top = Composite("top_menu")

sub2 = Child("submenu2")

top.append_child(sub1)

top.append_child(sub2)

top.component_function()
