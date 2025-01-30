from flask import session

from database.models import User
from functions.auth import hash_password, verify_password
from general import db


class UserService:
    @staticmethod
    def register(email, first_name, last_name, password):
        try:
            i = User(email=email, first_name=first_name, last_name=last_name, password=hash_password(password))
            db.session.add(i)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            # TODO: Add logging and better error handling here
            return False

    @staticmethod
    def login(email, password) -> bool:
        user = User.query.filter_by(email=email).first()
        if user:
            if verify_password(password, user.password):
                session["user_id"] = user.id
                session["user_email"] = user.email
                session["user_first_name"] = user.first_name
                session["user_last_name"] = user.last_name
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def get_all_users():
        return User.query.all()
