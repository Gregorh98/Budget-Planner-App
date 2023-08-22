from flask import Blueprint, render_template, redirect, url_for, request, flash

import db
import utils

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def index():
    return redirect(url_for("routes.home"))


@routes.route("/home")
def home():
    return render_template("home.html", pageTitle="Home")


# region incomes
@routes.route("/incomes/add", methods=["GET", "POST"])
def add_incomes():
    if request.method == "POST":
        try:
            data = utils.get_add_data_from_request(request.form)
            db.add_entry(data, "incomes")

            flash(("Added entry " + "'" + data['name'] + "'" + " successfully!"), "success")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")

    return render_template("add.html", pageTitle="Add Incomes")


@routes.route("/incomes/manage", methods=["GET", "POST"])
def manage_incomes():
    entries = db.get_all_entries("incomes")
    return render_template("manage.html", pageTitle="Manage Incomes", category="incomes", entries=entries)


@routes.route("/incomes/edit/<entry_id>", methods=["GET", "POST"])
def edit_income(entry_id):
    if request.method == "POST":
        try:
            data = utils.get_add_data_from_request(request.form)
            db.update_entry(entry_id, data, "incomes")

            flash(("Updated entry " + "'" + data['name'] + "'" + " successfully!"), "success")
            return redirect(url_for("routes.manage_incomes"))
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")

    entry = db.get_entry("incomes", entry_id)
    return render_template("edit.html", pageTitle="Edit Income", entry=entry)


# endregion

# region outgoings
@routes.route("/outgoings/add", methods=["GET", "POST"])
def add_outgoings():
    if request.method == "POST":
        try:
            data = utils.get_add_data_from_request(request.form)
            db.add_entry(data, "outgoings")

            flash(("Added entry " + "'" + data['name'] + "'" + " successfully!"), "success")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")

    return render_template("add.html", pageTitle="Add Outgoings")


@routes.route("/outgoings/manage", methods=["GET", "POST"])
def manage_outgoings():
    entries = db.get_all_entries("outgoings")
    return render_template("manage.html", pageTitle="Manage Outgoings", category="outgoings", entries=entries)


@routes.route("/outgoings/edit/<entry_id>", methods=["GET", "POST"])
def edit_outgoing(entry_id):
    if request.method == "POST":
        try:
            data = utils.get_add_data_from_request(request.form)
            db.update_entry(entry_id, data, "outgoings")

            flash(("Updated entry " + "'" + data['name'] + "'" + " successfully!"), "success")
            return redirect(url_for("routes.manage_outgoings"))
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")

    entry = db.get_entry("outgoings", entry_id)
    return render_template("edit.html", pageTitle="Edit Outgoing", entry=entry)


# endregion

# region savings-and-investments
@routes.route("/savings-and-investments/add", methods=["GET", "POST"])
def add_savings_and_investments():
    if request.method == "POST":
        try:
            data = utils.get_add_data_from_request(request.form)
            db.add_entry(data, "savings_and_investments")

            flash(("Added entry " + "'" + data['name'] + "'" + " successfully!"), "success")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")

    return render_template("add.html", pageTitle="Add Savings and Investments")


@routes.route("/savings-and-investments/manage", methods=["GET", "POST"])
def manage_savings_and_investments():
    entries = db.get_all_entries("savings_and_investments")
    return render_template("manage.html", pageTitle="Manage Savings and Investments",
                           category="savings-and-investments", entries=entries)


@routes.route("/savings-and-investments/edit/<entry_id>", methods=["GET", "POST"])
def edit_saving_or_investment(entry_id):
    if request.method == "POST":
        try:
            data = utils.get_add_data_from_request(request.form)
            db.update_entry(entry_id, data, "savings_and_investments")

            flash(("Updated entry " + "'" + data['name'] + "'" + " successfully!"), "success")
            return redirect(url_for("routes.manage_savings_and_investments"))
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")

    entry = db.get_entry("savings_and_investments", entry_id)
    return render_template("edit.html", pageTitle="Edit Saving or Investment", entry=entry)
# endregion
