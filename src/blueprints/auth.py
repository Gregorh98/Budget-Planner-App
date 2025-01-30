from flask import Blueprint, render_template, request, url_for, redirect, flash, session

from database.services import UserService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")

        if UserService.register(email, first_name, last_name, password):
            flash("Account created successfully, please log in", "success")
            return redirect(url_for("auth.login"))

        return redirect(url_for("auth.register"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if UserService.login(email, password):
            print("HIT")
            return redirect(url_for("general.index"))
        else:
            flash("Username or Password is incorrect", "danger")
            return redirect(url_for("auth.login"))
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.index"))
