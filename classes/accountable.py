from enums import Interval


class Accountable:
    def __init__(self, name, value, start_date, end_date=None, interval=Interval.Once):
        self.name = name
        self.value = value
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval

    def __repr__(self):
        return f"{self.name} - {self.value}"

    def __str__(self):
        return self.name
