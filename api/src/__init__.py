from flask import Flask
from routes.index import main
from models.db import db
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="api/.env")

def create_app():

    app = Flask(__name__)
    app.register_blueprint(main)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("connection_string")
    db.init_app(app)

    return [app,db] 
