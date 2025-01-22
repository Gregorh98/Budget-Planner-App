from flask import Flask

from blueprints import auth_bp, general_bp
from database.crud import init_database

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(general_bp)

if __name__ == '__main__':
    init_database()
    app.run(host="0.0.0.0", port=5000)
