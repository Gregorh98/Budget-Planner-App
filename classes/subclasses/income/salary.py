from classes import BaseIncome


class Salary(BaseIncome):
    def __init__(self, name, value, start_date, interval, end_date=None):
        super().__init__(name, value, start_date, interval, end_date)