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
