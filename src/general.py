import os
import secrets

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.models.base import Base

load_dotenv()

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.secret_key = secrets.token_urlsafe(16)

db.init_app(app)
