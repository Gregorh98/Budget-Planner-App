from flask import session

from database.models import Expense
from general import db


class ExpenseService:
    @staticmethod
    def add(name, value, start_date, end_date, interval):
        i = Expense(
            session.get("user_id"),
            name=name,
            value=value,
            start_date=start_date,
            end_date=end_date,
            interval=interval
        )

        db.session.add(i)
        db.session.commit()
        return "User added successfully."

    @staticmethod
    def get_all():
        return Expense.query.filter_by(user_id=session.get("user_id")).first()
