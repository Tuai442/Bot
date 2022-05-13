import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"
app = Flask(__name__)

def create_app():
    app.config['SECRET_KEY'] = "test"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #db.init_app(app)

    # Voeg hier nieuwe pagina's toe:
    from View.auth import auth
    app.register_blueprint(auth, url_prefix="/")

    from View.index import index
    app.register_blueprint(index, url_prefix="/")

    from View.Models.user import User
    dir = os.getcwd()
    if not path.exists(dir + "/View/" + DB_NAME):
        db.create_all(app=app)
        print("Databank is gemaakt")

    from View.Models.user import User

    return app






