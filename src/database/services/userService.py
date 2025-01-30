import logging

from flask import session
from sqlalchemy.exc import IntegrityError

from database.models import User
from functions.auth import hash_password, verify_password
from general import db


class UserService:
    @staticmethod
    def register(email, first_name, last_name, password):
        logging.info(f"Registering user: {email}")
        try:
            i = User(email=email, first_name=first_name, last_name=last_name, password=hash_password(password))
            db.session.add(i)
            db.session.commit()
            return {"status": True, "message": "Account created successfully, please log in"}
        except Exception as e:
            db.session.rollback()

            if isinstance(e, IntegrityError):
                message = "An account with that email already exists"
            else:
                message = str(e)

            logging.error(f"Failed to register user: {e}")
            return {"status": False, "message": message}

    @staticmethod
    def login(email, password) -> dict:
        user = User.query.filter_by(email=email).first()
        if user:
            if verify_password(password, user.password):
                session["user_id"] = user.id
                session["user_email"] = user.email
                session["user_first_name"] = user.first_name
                session["user_last_name"] = user.last_name
                return {"status": True, "message": "Logged in successfully"}
            else:
                return {"status": False, "message": "Email or Password is incorrect"}
        else:
            return {"status": False, "message": "No user with that email exists. Did you mean to register?"}

    @staticmethod
    def get_all_users():
        return User.query.all()
