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
        return redirect(url_for("routes.add_incomes"))

    return render_template("add.html", pageTitle="Add Incomes")


@routes.route("/incomes/manage", methods=["GET", "POST"])
def manage_incomes():
    return render_template("manage.html", pageTitle="Manage Incomes")


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
        return redirect(url_for("routes.add_outgoings"))

    return render_template("add.html", pageTitle="Add Outgoings")


@routes.route("/outgoings/manage", methods=["GET", "POST"])
def manage_outgoings():
    return render_template("manage.html", pageTitle="Manage Outgoings")


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
        return redirect(url_for("routes.add_savings_and_investments"))

    return render_template("add.html", pageTitle="Add Savings and Investments")


@routes.route("/savings-and-investments/manage", methods=["GET", "POST"])
def manage_savings_and_investments():
    return render_template("manage.html", pageTitle="Manage Savings and Investments")
# endregion
