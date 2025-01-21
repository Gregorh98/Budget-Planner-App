from datetime import date, timedelta

from classes import Budget
from classes.subclasses.income import Salary
from enums import Interval

b = Budget()
b.incomes.append(Salary("Flexitricity Salary", 2487.70, start_date=date(2025, 1, 19), interval=Interval.Yearly))

p = b.get_budget_breakdown(date.today(), date.today() + timedelta(days=1095))
print(p)
