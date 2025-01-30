from functools import wraps

import bcrypt
from flask import session, redirect, url_for


def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("username"):
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password  # Returns bytes


def verify_password(test_password, db_password):
    return bcrypt.checkpw(test_password.encode("utf-8"), db_password)
