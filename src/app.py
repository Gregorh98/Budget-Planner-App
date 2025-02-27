import logging
import time

from sqlalchemy.exc import IntegrityError, OperationalError

from blueprints import auth_bp, general_bp
from database.models import *  # NOQA
from database.services import UserService
from general import app, db

if __name__ == '__main__':
    logging.basicConfig(filename="log.dat",
                        filemode='a',
                        format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)

    logging.info("Registering blueprints")
    app.register_blueprint(auth_bp)
    app.register_blueprint(general_bp)

    with app.app_context():
        logging.info("Creating database structure")
        while True:
            try:
                db.create_all()
                break
            except OperationalError:
                logging.log(logging.WARN, "Database connection failed. Retrying in 1 second.")
                time.sleep(1)

        try:
            logging.info("Registering default user")
            UserService.register("test.user@test.com", "Test", "User", "password123")
        except IntegrityError as e:
            logging.error("Failed to register default user")
            db.session.rollback()

    app.run(host="0.0.0.0", port=5000)
