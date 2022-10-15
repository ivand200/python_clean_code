"""Properties"""
# For example, if you have an object that needs to return a value in a particular format,
# or data type, a property can be used to do this computation. In the previous example,
# if we decided that we wanted to return the coordinates with a precision of up to four
# decimal places (regardless of how many decimal places the original number was
# provided with), we can make the computation for rounding this in the @property
# method that reads the value.

# You might find that properties are a good way to achieve command and query
# separation ( CC08 ). The command and query separation principle states that a method
# of an object should either answer to something or do something, but not both. If a
# method is doing something, and at the same time it returns a status answering a
# question of how that operation went, then it's doing more than one thing, clearly
# violating the principle that says that functions should do one thing, and one thing
# only.

# Another piece of good advice derived from this example is as follows—don't do
# more than one thing in a method. If you want to assign something and then check
# the value, break that down into two or more statements.

# Methods should do one thing only. If you have to run an action
# and then check for the status, do that in separate methods that are
# called by different statements.

# To illustrate what this means, using the previous example, we would have one
# setter or getter method, to set the email of the user, and then another property to
# simply ask for the email.


from typing import Optional


class Coordinate:
    """
    Property decorator example
    """

    def __init__(self, lat: float, long: float) -> None:
        self._latitude = self._longitude = None
        self.latitude = lat
        self.longitude = long

    @property
    def latitude(self):
        """Returns _latitude"""
        return self._latitude

    @latitude.setter
    def latitude(self, lat_value: float) -> None:
        if lat_value not in range(-90, 90 + 1):
            raise ValueError(f"{lat_value} is an invalid value for latitude")
        self._latitude = lat_value

    @property
    def longitude(self) -> Optional[float]:
        """Return _longitude"""
        return self._longitude

    @longitude.setter
    def longitude(self, long_value: float) -> None:
        if long_value not in range(-180, 180 + 1):
            raise ValueError(f"{long_value} is an invalid value for longitude")
        self._longitude = long_value


cor = Coordinate(85, 90)
cor_2 = Coordinate(102, 165)
print(cor.latitude, cor.longitude)
print(cor_2.latitude)


# class Alphabet:
#     def __init__(self, value):
#         self._value = value

#     # getting the values
#     @property
#     def value(self):
#         print('Getting value')
#         return self._value

#     # setting the values
#     @value.setter
#     def value(self, value):
#         print('Setting value to ' + value)
#         self._value = value

#     # deleting the values
#     @value.deleter
#     def value(self):
#         print('Deleting value')
#         del self._value
