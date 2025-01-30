from flask import session

from database.models import Income
from general import db


class IncomeService:
    @staticmethod
    def add(name, value, start_date, end_date, interval):
        i = Income(
            session.get("user_id"),
            name=name,
            value=value,
            start_date=start_date,
            end_date=end_date,
            interval=interval
        )

        db.session.add(i)
        db.session.commit()
        return i

    @staticmethod
    def get_all():
        return Income.query.filter_by(user_id=session.get("user_id")).first()
