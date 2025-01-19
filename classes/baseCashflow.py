from datetime import date, timedelta

from enums import Interval


class BaseCashflow:
    def __init__(self, name, value, start_date, end_date=None, interval=Interval.Once):
        self.name = name
        self.value = value
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval

    def __repr__(self):
        return f"{self.name} - {self.value} - {self.interval}"

    def __str__(self):
        return self.name

    def get_next_due_date(self, start_date=date.today()):
        if self.interval == Interval.Once:
            return self.start_date
        elif self.interval == Interval.Daily:
            return start_date + timedelta(days=1)
        elif self.interval == Interval.Weekly:
            days_since_start = (start_date - self.start_date).days
            next_due_days = (7 - (days_since_start % 7)) % 7
            next_date = start_date + timedelta(days=next_due_days)
            return next_date
        elif self.interval == Interval.Monthly:
            if start_date.day > self.start_date.day:
                next_month = (start_date.month % 12) + 1
                year_adjustment = start_date.year + (start_date.month // 12)
            else:
                next_month = start_date.month
                year_adjustment = start_date.year
            d = date(year_adjustment, next_month, self.start_date.day)
            return d
        elif self.interval == Interval.Yearly:
            if start_date > date(start_date.year, self.start_date.month, self.start_date.day):
                d = date(start_date.year + 1, self.start_date.month, self.start_date.day)
            else:
                d = date(start_date.year, self.start_date.month, self.start_date.day)
            print(start_date, d)
            return d
        else:
            raise ValueError(f"Unsupported interval: {self.interval}")
