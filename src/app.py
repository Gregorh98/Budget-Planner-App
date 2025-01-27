from database.models import *  # NOQA
from database.services import DatabaseService
from general import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        DatabaseService.init_db()

    app.run(host="0.0.0.0", port=5000)
