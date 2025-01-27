import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blueprints import auth_bp, general_bp
from database.models import Base

load_dotenv()

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

app.register_blueprint(auth_bp)
app.register_blueprint(general_bp)

db.init_app(app)
