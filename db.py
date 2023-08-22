import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def getConn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )


def add_income(income_data):
    with getConn() as conn:
        with conn.cursor() as cursor:
            sql = "insert into public.incomes (userid, name, amount, note, date, repeats_monthly, repeats_annually, repeats_weekly) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (
                0,  # TODO: Replace with real user id
                income_data["name"],
                income_data["amount"],
                income_data["note"],
                income_data["date"],
                True if income_data["repeats"] == "monthly" else False,
                True if income_data["repeats"] == "annually" else False,
                True if income_data["repeats"] == "weekly" else False,
            )

            cursor.execute(sql, data)
            conn.commit()
