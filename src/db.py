
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv(find_dotenv())

def configure_db(app):
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    
    return db