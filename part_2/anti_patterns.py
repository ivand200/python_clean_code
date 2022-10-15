"""
Do not use mutable objects as default arguments
The fix is simple - use None as a default sentinel value
"""
def user_display(user_metadata: dict = None):
    user_metadata = user_metadata or {"name": "John", "age": 30}
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"


"""
Extendig built-in types
Don't extend directly from dict, use collections.UserDict instead.
For list, use collections.UserList
For strings, use collections.UserString
"""

from collections import UserList


class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "even"
        else:
            prefix = "odd"
        return f"[{prefix}] {value}"


gl = GoodList((0, 1, 2))
print(gl[0])
print(gl[1])
print(gl[2])


