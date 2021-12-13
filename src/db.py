import os
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())


def configure_db(app):
    uri = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db
