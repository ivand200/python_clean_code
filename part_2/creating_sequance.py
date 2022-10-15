"""Creating sequence"""
from datetime import timedelta, date


class DateRangeSequance:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


seq = DateRangeSequance(date(2020, 1, 1), date(2022, 1, 1))
for day in seq:
    print(day)


print(seq[5])
print(seq[-6])