from database.models import User
from general import db


class UserService:
    @staticmethod
    def add_user(email, first_name, last_name, password):
        user = User(email=email, first_name=first_name, last_name=last_name, password=password)
        db.session.add(user)
        db.session.commit()
        return "User added successfully."

    @staticmethod
    def get_user(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_all_users():
        return User.query.all()
