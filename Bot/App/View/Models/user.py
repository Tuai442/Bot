from flask_login import UserMixin
from sqlalchemy.sql import func
from View import db
from werkzeug.security import generate_password_hash, check_password_hash

# create table user(id int primary key, email string unique, username string unique, password string, date_created Date);

class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

