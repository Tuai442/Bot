import os
import re
from datetime import datetime
from os import path

import bcrypt
from flask import flash
from flask_bcrypt import generate_password_hash, check_password_hash, Bcrypt
from flask_login import LoginManager, login_manager
from flask_sqlalchemy import SQLAlchemy

from Bot.App.Domain.Models.singletonDecorader import singleton
from Bot.App.View.Models.user import User

#TODO: van type enums maken
class Message:
    def __init__(self, msg, type=None):
        self._msg = msg
        self._type = type

    @property
    def type(self):
        return self._type

    @property
    def msg(self):
        return self._msg

    def __repr__(self):
        return self._msg




@singleton
class Validator:
    def __init__(self):
        self._DB_NAME = "database.db"
        self._email_pattern = '^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$'
        self._pass_pattern = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'

    def validate_user(self, username: str, email: str, pass1: str, pass2: str) -> Message:
        if not self._check_username(username):
            return Message("Gebruikersnaam is bestaad al of is te kort (username > 4)", 'error')

        if not self._check_email(email):
            return Message("Email bestaad al of is niet in het correcte formaat.", 'error')

        if not self._check_pass(pass1, pass2):
            return Message("De paswoorden zijn niet gelijk aan elkaar of zijn niet in het juiste formaat,"
                   "(Minimum 8 karakters en minstens 1 letter en 1 nummer.", 'error')

        return Message("Gebruiker is aangemaakt")

    def _check_username(self, username: str) -> bool:
        username_exists = User.query.filter_by(username=username).first()
        if not username_exists and len(username) > 2:
            return True
        return False

    def _check_email(self, email: str) -> bool:
        email_exists = User.query.filter_by(email=email).first()
        if re.match(self._email_pattern, email) and email_exists is None:
            return True
        return False

    def _check_pass(self, pass1: str, pass2: str) -> bool:
        if pass1 == pass2 and re.match(self._pass_pattern, pass1):
            return True
        return False

