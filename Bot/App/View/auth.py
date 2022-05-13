from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, Flask
from flask_login import login_user, logout_user, login_required, LoginManager

from View import db, app
from View.Forms.autherize_form import LoginForm, RegistrationForm
from passlib.hash import sha256_crypt
from flask_bcrypt import Bcrypt

import datetime

from View.Models.user import User

bcrypt = Bcrypt(app)
# De login manager in een library van flask die de toegang regeld van pagina's,
# Bv: je kan niet je accounts ww veranderen als je niet ben ingelogd.
login_manager = LoginManager()
login_manager.login_view = "routes.login"
login_manager.init_app(app)
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(id: int):
    if id is None:
        return User.query.get(id)
    else:
        return None


auth = Blueprint("auth", __name__,
                 template_folder='templates',
                 static_folder='static',
                 static_url_path='styles')

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # if message.type == "error":
        #     print(message.msg)
        #     return render_template("login.html", form=form)
        # else:
        #     print(message.msg)
        #     return redirect(url_for("index.home"))

    return render_template("login.html", form=form)

@auth.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        try:
            email = form.email.data
            username = form.username.data
            password = form.password.data
            hashed_password =   bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(email=email, username=username, password=hashed_password, date_created=datetime.now())
            db.session.add(new_user)
            db.session.commit()
            
            login_user(new_user)
            return redirect(url_for("index.home"))

        except Exception as e:
            print(e)

    return render_template("registration.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("views.home"))


