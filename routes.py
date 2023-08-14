from flask import Blueprint, render_template

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def index():
    return render_template("index.html", pageTitle="Home")


@routes.route("/incomes/manage")
def manage_incomes():
    return render_template("manage-incomes.html", pageTitle="Manage Incomes")


@routes.route("/outgoings/manage")
def manage_outgoings():
    return render_template("manage-outgoings.html", pageTitle="Manage Outgoings")


@routes.route("/savings-and-investments/manage")
def manage_savings_and_investments():
    return render_template("manage-savings-and-investments.html", pageTitle="Manage Savings and Investments")
