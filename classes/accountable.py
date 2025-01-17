class Accountable:
    def __init__(self, name, value, start_date):
        self.name = name
        self.value = value
        self.start_date = start_date

    def __repr__(self):
        return f"{self.name} - {self.value}"

    def __str__(self):
        return self.name
