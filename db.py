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
            sql = "insert into %s (user_id, name, amount, note, start_date, end_date, repeats_monthly, repeats_annually, repeats_weekly) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (
                AsIs("public." + target_table),
                0,  # TODO: Replace with real user id
                entry_data["name"],
                entry_data["amount"],
                entry_data["note"],
                entry_data["start_date"],
                None if entry_data["end_date"] == "" else entry_data["end_date"],
                True if entry_data["repeats"] == "monthly" else False,
                True if entry_data["repeats"] == "annually" else False,
                True if entry_data["repeats"] == "weekly" else False,
            )

            cursor.execute(sql, data)
            conn.commit()


def get_all_entries(target_table):
    with getConn() as conn:
        with conn.cursor() as cursor:
            sql = "select id, name, amount, note, start_date, end_date, repeats_monthly, repeats_annually, repeats_weekly from %s where user_id = %s order by id asc"
            data = (
                AsIs("public." + target_table),
                0  # TODO: Replace with real user id
            )

            cursor.execute(sql, data)

            results = cursor.fetchall()

            entries = []
            for result in results:
                entries.append(
                    {"id": result[0],
                     "name": result[1],
                     "amount": result[2],
                     "note": result[3],
                     "start_date": result[4],
                     "end_date": result[5],
                     "repeats_monthly": result[6],
                     "repeats_annually": result[7],
                     "repeats_weekly": result[8]
                     }
                )

            return entries


def get_entry(target_table, entry_id):
    with getConn() as conn:
        with conn.cursor() as cursor:
            sql = "select id, name, amount, note, start_date, end_date, repeats_monthly, repeats_annually, repeats_weekly from %s where user_id = %s and id = %s"
            data = (
                AsIs("public." + target_table),
                0,  # TODO: Replace with real user id
                entry_id
            )

            cursor.execute(sql, data)

            result = cursor.fetchone()

            entry = {"id": result[0],
                     "name": result[1],
                     "amount": result[2],
                     "note": result[3],
                     "start_date": result[4],
                     "end_date": result[5],
                     "repeats_monthly": result[6],
                     "repeats_annually": result[7],
                     "repeats_weekly": result[8]
                     }

            return entry


def update_entry(entry_id, entry_data, target_table):
    with getConn() as conn:
        with conn.cursor() as cursor:
            sql = "update %s set name = %s, amount = %s, note = %s, start_date = %s, end_date = %s, repeats_monthly = %s, repeats_annually = %s, repeats_weekly = %s where id = %s and user_id = %s"
            data = (
                AsIs("public." + target_table),
                entry_data["name"],
                entry_data["amount"],
                entry_data["note"],
                entry_data["start_date"],
                None if entry_data["end_date"] == "" else entry_data["end_date"],
                True if entry_data["repeats"] == "monthly" else False,
                True if entry_data["repeats"] == "annually" else False,
                True if entry_data["repeats"] == "weekly" else False,
                entry_id,
                0  # TODO: Replace with real user id
            )

            cursor.execute(sql, data)
            conn.commit()
