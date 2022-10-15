"""KIS"""


class Namespace:
    """Create an object from keyword arguments"""

    ACCEPTED_VALUES = ("id_", "user", "location")

    def __init__(self, **data):
        for attr_name, attr_value in data.items():
            if attr_name in self.ACCEPTED_VALUES:
                setattr(self, attr_name, attr_value)


cn = Namespace(id_=42, user="root", location="127.0.0.1")
print(cn.id_)
print(cn.user)