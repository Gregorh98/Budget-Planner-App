from flask import Blueprint, render_template

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def index():
    return render_template("index.html", pageTitle="Home")


@routes.route("/manage/manage-incomes")
def manage_incomes():
    return render_template("manage-incomes.html", pageTitle="Manage Incomes")


@routes.route("/manage/manage-outgoings")
def manage_outgoings():
    return render_template("manage-outgoings.html", pageTitle="Manage Outgoings")


@routes.route("/manage/manage-savings-and-investments")
def manage_savings_and_investments():
    return render_template("manage-savings-and-investments.html", pageTitle="Manage Savings and Investments")
