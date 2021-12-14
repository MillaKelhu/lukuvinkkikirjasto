from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv(find_dotenv())


def configure_db(app):
    uri = os.environ.get("SQLITE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    dbpath = "../main.db"
    schema_path = "../schema.sql"
    os.system(f"sqlite3 {dbpath} < {schema_path}")
    return db
