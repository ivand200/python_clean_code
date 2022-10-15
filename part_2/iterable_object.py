"""Iterable_object"""
# At this point, Python
# will call the iter() function on it, which, in turn, will call the __iter__ magic
# method. On this method, it is defined to return self , indicating that the object is an
# iterable itself, so at that point every step of the loop will call the next() function
# on that object, which delegates to the __next__ method. In this method, we decide
# how to produce the elements and return one at a time.


from datetime import timedelta, date


class DateRangeIterable:
    """
    An iterable that contains its own iterator object
    """

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration()
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class DateRangeContainerIterable:
    """Container iterable"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


days = DateRangeIterable(date(2018, 1, 1), date(2018, 2, 5))
for day in days:
    print(day)


days_2 = DateRangeContainerIterable(date(2018, 1, 1), date(2020, 1, 5))
for i in days_2:
    print(i)
