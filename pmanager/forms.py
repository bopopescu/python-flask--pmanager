from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], id="task-title")
    description = TextAreaField('Content', id="task-description")
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    name = StringField('Username', id="username-filed")
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], id="username-filled")
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
