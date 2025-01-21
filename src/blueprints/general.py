from flask import Blueprint, redirect, url_for

from functions.auth import require_auth

general_bp = Blueprint("general_bp", __name__)


@general_bp.route('/')
def index():
    return redirect(url_for('general_bp.home'))


@general_bp.route('/home')
@require_auth
def home():
    return "Home"
