class Borg:

    """The Borg design pattern"""

    _shared_data = {}  # Attribute dictionary

    def __init__(self):

        self.__dict__ = self._shared_data  # make an attribute dictionary


class Singleton(Borg):
    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)

        # Update the attribute dict by insertting new key/value pair
        self._shared_data.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_data)  # print attribute dictionary


x = Singleton(HTTP="Hyper text transfer protocol")
y = Singleton(SNMP='Simple Network Management Protocol')

print(y)
