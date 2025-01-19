from classes import BaseSaving


class LongTerm(BaseSaving):
    def __init__(self, name, value, start_date, interval, end_date=None):
        super().__init__(name, value, start_date, end_date, interval)
