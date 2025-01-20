from src.classes import BaseOutgoing


class Fixed(BaseOutgoing):
    def __init__(self, name, value, start_date, interval, end_date=None):
        super().__init__(name, value, start_date, end_date, interval, fixed=True)
