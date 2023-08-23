from datetime import datetime


def get_add_data_from_request(form_data):
    data = {
        "name": form_data.get("name"),
        "amount": int(form_data.get("amount")) if form_data.get("amount") != "" else "",
        "start_date": form_data.get("start_date"),
        "end_date": form_data.get("end_date"),
        "repeats": form_data.get("repeats"),
        "note": form_data.get("note")
    }
    print(data)

    validate_data(data)

    return data


def validate_data(data):
    if data["name"] == "" or data["name"] == None:
        raise Exception("Please enter a valid name")

    if data["amount"] == '' or data["amount"] == None or data["amount"] <= 0:
        raise Exception("Please enter a valid amount")

    if data["start_date"] == "" or data["start_date"] == None:
        raise Exception("Please set a start date")

    if data["end_date"] != "" and data["end_date"] != None:
        if data["start_date"] > data["end_date"]:
            raise Exception("Please make sure start date is after end date")


def get_months():
    currentMonth = datetime.today().month

    months = [
        {"number": 1, "as_text": "January", "short_text": "Jan"},
        {"number": 2, "as_text": "February", "short_text": "Feb"},
        {"number": 3, "as_text": "March", "short_text": "Mar"},
        {"number": 4, "as_text": "April", "short_text": "Apr"},
        {"number": 5, "as_text": "May", "short_text": "May"},
        {"number": 6, "as_text": "June", "short_text": "Jun"},
        {"number": 7, "as_text": "July", "short_text": "Jul"},
        {"number": 8, "as_text": "August", "short_text": "Aug"},
        {"number": 9, "as_text": "September", "short_text": "Sep"},
        {"number": 10, "as_text": "October", "short_text": "Oct"},
        {"number": 11, "as_text": "November", "short_text": "Nov"},
        {"number": 12, "as_text": "December", "short_text": "Dec"},
    ]

    for month in months:
        month["active"] = True if currentMonth <= month["number"] else False
        month["is_current"] = True if currentMonth == month["number"] else False

    return months
