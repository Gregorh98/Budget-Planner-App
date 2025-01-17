from classes import Accountable


class Income(Accountable):
    def __init__(self, name, value, start_date=None):
        super().__init__(name, value, start_date)
