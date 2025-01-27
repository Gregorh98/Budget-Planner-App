from database.services import UserService


class DatabaseService:
    @staticmethod
    def init_db():
        UserService.add_user("gregor.hastings@outlook.com", "Gregor", "Hastings", "password123")
