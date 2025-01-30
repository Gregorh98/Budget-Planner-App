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

        # Check for "nones"
        print(first_name)
        if any(param in [None, ""] for param in [first_name, last_name, email, password]):
            flash("Please fill in all fields", "danger")
            return redirect(url_for("auth.register"))

        # Attempt to register the user
        reg = UserService.register(email, first_name, last_name, password)

        flash(reg.get("message"), "success" if reg.get("status") else "danger")
        return redirect(url_for("auth.login" if reg.get("status") else "auth.register"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        attempt = UserService.login(email, password)
        if attempt.get("status"):
            return redirect(url_for("general.index"))
        else:
            flash(attempt.get("message"), "danger")
            return redirect(url_for("auth.login"))
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.index"))
