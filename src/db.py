from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv(find_dotenv())


def configure_db(app):
    uri = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://///Users/rikumattila/lukuvinkkikirjasto/lukuvinkkikirjasto.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db
