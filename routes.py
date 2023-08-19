from flask import Blueprint, render_template, redirect, url_for

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def index():
    return redirect(url_for("routes.home"))


@routes.route("/home")
def home():
    return render_template("home.html", pageTitle="Home")


@routes.route("/incomes/add")
def add_incomes():
    return render_template("add.html", pageTitle="Add Incomes")


@routes.route("/incomes/manage")
def manage_incomes():
    return render_template("manage.html", pageTitle="Manage Incomes")


@routes.route("/outgoings/add")
def add_outgoings():
    return render_template("add.html", pageTitle="Add Outgoings")


@routes.route("/outgoings/manage")
def manage_outgoings():
    return render_template("manage.html", pageTitle="Manage Outgoings")


@routes.route("/savings-and-investments/add")
def add_savings_and_investments():
    return render_template("add.html", pageTitle="Add Savings and Investments")


@routes.route("/savings-and-investments/manage")
def manage_savings_and_investments():
    return render_template("manage.html", pageTitle="Manage Savings and Investments")
