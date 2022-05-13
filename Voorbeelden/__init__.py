from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
DB_NAME = "database.db"
app = Flask(__name__)

def create_app():
    app.config['SECRET_KEY'] = "test"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #db.init_app(app)

    # Voeg hier nieuwe pagina's to
    from index import index
    app.register_blueprint(index, url_prefix="/")


    return app






