from datetime import date

from classes import Income, Outgoing
from enums import Interval
from enums.outgoing_category import Outgoing_Category


class Budgie():
    def __init__(self, save=None):
        self.name = "New Budget"
        self.incomes = []
        self.outgoings = []
        self.investments = []
        self.savings = []

        if save:
            self.load_save(save)

    def __str__(self):
        return self.name

    # region IO
    def load_save(self, save):
        self.incomes = save["incomes"]
        self.investments = save["investments"]
        self.savings = save["savings"]
        self.rolling_expenses = save["rolling_expenses"]
        self.committed_expenses = save["committed_expenses"]
        self.uncommitted_expenses = save["uncommitted_expenses"]

    def export_save(self):
        save = {
            "incomes": self.incomes,
            "investments": self.investments,
            "savings": self.savings,
            "rolling_expenses": self.rolling_expenses,
            "committed_expenses": self.committed_expenses,
            "uncommitted_expenses": self.uncommitted_expenses,
        }

    # endregion

    # region Incomes
    def add_income(self, name, amount, start_date=date.today(), end_date=None, interval=Interval.Once):
        self.incomes.append(Income(name, amount, start_date, interval, end_date))

    # endregion

    # region Outgoings
    def add_committed_outgoing(self, name, amount, start_date=date.today(), end_date=None, interval=Interval.Once):
        self.outgoings.append(Outgoing(name, amount, start_date, interval, Outgoing_Category.Committed, end_date))

    def add_flexible_outgoing(self, name, amount, start_date=date.today(), end_date=None, interval=Interval.Once):
        self.outgoings.append(Outgoing(name, amount, start_date, Outgoing_Category.Flexible, interval, end_date))
    # endregion


b = Budgie()
print(b)
b.add_income("Salary", 2487.70, interval=Interval.Monthly, start_date=date(2023, 5, 28))
print(b.incomes)

print(b.incomes[0].get_next_due_date())
