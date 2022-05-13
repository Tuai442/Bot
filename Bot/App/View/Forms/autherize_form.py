from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from flask_wtf import FlaskForm



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[
        DataRequired(),
        Regexp('^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$', message="Email is niet in het correct formaat.")])
    password = PasswordField("Password", validators=[
        DataRequired(),
        EqualTo('confirm', message="Passworden moeten gelijk zijn aan elkaar"),
        Regexp('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', message="Minimum 8 karakters en minstens 1 letter en 1 nummer."),])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), ])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

