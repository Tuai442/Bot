from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf import FlaskForm


class StrategySetupForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])



class FibonacciSetupForm(FlaskForm):
    name = StringField('Naam', validators=[DataRequired(), Length(min=2, max=20)])
    init_date = StringField('Start Set', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField("Instellen")

class RsiSetupForm(FlaskForm):
    name = StringField('Naam', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField("Instellen")