import os

import psycopg2
from dotenv import load_dotenv
from psycopg2._psycopg import AsIs

load_dotenv()


def getConn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )


def add_entry(entry_data, target_table):
    with getConn() as conn:
        with conn.cursor() as cursor:
            sql = "insert into %s (userid, name, amount, note, date, repeats_monthly, repeats_annually, repeats_weekly) values (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (
                AsIs("public." + target_table),
                0,  # TODO: Replace with real user id
                entry_data["name"],
                entry_data["amount"],
                entry_data["note"],
                entry_data["date"],
                True if entry_data["repeats"] == "monthly" else False,
                True if entry_data["repeats"] == "annually" else False,
                True if entry_data["repeats"] == "weekly" else False,
            )

            cursor.execute(sql, data)
            conn.commit()
