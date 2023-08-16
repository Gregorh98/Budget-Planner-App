from flask import Blueprint, render_template, request, redirect, url_for, flash

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def index():
    return render_template("index.html", pageTitle="Home")


@routes.route("/incomes/manage")
def manage_incomes():
    return render_template("incomes/manage-incomes.html", pageTitle="Manage Incomes")


@routes.route("/incomes/add", methods=["GET", "POST"])
def add_incomes():
    if request.method == "POST":
        flash("HIT")
        return redirect(url_for("routes.add_incomes"))
    return render_template("incomes/add-incomes.html", pageTitle="Add Income")


@routes.route("/outgoings/manage")
def manage_outgoings():
    return render_template("outgoings/manage-outgoings.html", pageTitle="Manage Outgoings")


@routes.route("/outgoings/add")
def add_outgoings():
    return render_template("outgoings/add-outgoings.html", pageTitle="Add Outgoings")


@routes.route("/savings-and-investments/manage")
def manage_savings_and_investments():
    return render_template("savings-and-investments/manage-savings-and-investments.html",
                           pageTitle="Manage Savings and Investments")


@routes.route("/savings-and-investments/add")
def add_savings_and_investments():
    return render_template("savings-and-investments/add-savings-and-investments.html",
                           pageTitle="Add Savings and Investments")
