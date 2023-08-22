def get_add_data_from_request(form_data):
    data = {
        "name": form_data.get("name"),
        "amount": form_data.get("amount"),
        "date": form_data.get("date"),
        "repeats": form_data.get("repeats"),
        "note": form_data.get("note")
    }

    return data
