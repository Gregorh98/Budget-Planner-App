from flask import Blueprint, redirect, url_for, render_template

from functions.auth import require_auth

general_bp = Blueprint("general", __name__)


@general_bp.route('/')
def index():
    return redirect(url_for('general.home'))


@general_bp.route('/home')
@require_auth
def home():
    return render_template('home.html')
