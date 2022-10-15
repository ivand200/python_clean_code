"""Creating your own sequences"""


# A sequence is an object that implements both __getitem__ and __len__
# method __getitem__ -> is called when myobject[key] is called.
# Passing the key as a parameter.

from collections.abc import Sequence


class Items(Sequence):
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)

    def best(self):
        return max(self._values)

    
dates = Items(3, 4, 5, 6, 7, 8, 9)
print(dates.best())