from functools import wraps

from flask import session, redirect, url_for


def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("username"):
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function
