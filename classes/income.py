from datetime import date

from classes import Accountable
from enums import Interval


class Income(Accountable):
    def __init__(self, name, value, start_date=date.today(), end_date=None, interval=Interval.Once):
        super().__init__(name, value, start_date, end_date, interval)
