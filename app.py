import json
import pickle
from datetime import date, timedelta

from classes.subclasses.income import Salary
from enums import Interval


class Budget:
    def __init__(self, save=None):
        self.name = "New Budget"
        self.incomes = []
        self.outgoings = []
        self.savings = []

        if save:
            self.load_save(save)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name, self.incomes, self.outgoings, self.savings

    # region IO
    def load_save(self, save_file):
        with open(save_file, "rb") as file:
            save = pickle.load(file)
            self.name = save.name
            self.incomes = save.incomes
            self.outgoings = save.outgoings
            self.savings = save.savings

    def export_save(self):
        with open('save.pkl', 'wb') as file:
            pickle.dump(self, file)

    # endregion

    # region Budget
    def get_budget_breakdown(self, start_date, end_date):
        schedule = []
        date_iq = start_date

        while date_iq <= end_date:
            schedule.append({
                "date": date_iq.strftime('%Y-%m-%d'),
                "incomes": [x for x in self.incomes if x.get_next_due_date(date_iq) == date_iq],
                "outgoings": [x for x in self.outgoings if x.get_next_due_date(date_iq) == date_iq],
                "savings": [x for x in self.savings if x.get_next_due_date(date_iq) == date_iq]
            })

            date_iq += timedelta(days=1)  # Properly increment date_iq

        return schedule

    # endregion


b = Budget()
b.incomes.append(Salary("Flexitricity Salary", 2487.70, start_date=date(2025,1,19), interval=Interval.Yearly))

p = b.get_budget_breakdown(date.today(), date.today()+timedelta(days=1095))
print(p)
