from sqlalchemy.exc import IntegrityError

from blueprints import auth_bp, general_bp
from database.models import *  # NOQA
from database.services import UserService
from general import app, db

if __name__ == '__main__':
    app.register_blueprint(auth_bp)
    app.register_blueprint(general_bp)

    with app.app_context():
        db.create_all()
        try:
            UserService.register("gregor.hastings@outlook.com", "Gregor", "Hastings", "password123")
        except IntegrityError as e:
            db.session.rollback()

    app.run(host="0.0.0.0", port=5000)
