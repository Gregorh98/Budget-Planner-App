from database.models import User
from general import db


class UserService:
    @staticmethod
    def add_user(email, first_name, last_name, password):
        i = User(email=email, first_name=first_name, last_name=last_name, password=password)
        db.session.add(i)
        db.session.commit()
        return i

    @staticmethod
    def get_user(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all_users():
        return User.query.all()
