from classes import Income


class Budgie():
    def __init__(self, save):
        self.incomes = []
        self.investments = []
        self.savings = []
        self.rolling_expenses = []
        self.committed_expenses = []
        self.uncommitted_expenses = []

        if save:
            self.load_save(save)

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
    def add_income(self, name, amount):
        self.incomes.append({"name": name, "amount": amount, "repeat": True, "interval": 12})


i = Income("TEST", 123)
