import os

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from database import Base

Engine = create_engine(os.getenv("DATABASE_URL"))


def init_database():
    if not database_exists(Engine.url):
        create_database(Engine.url)

    Base.metadata.create_all(Engine)
