from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from models import User

def invalid_credentials(form, field):
    """ Username and Password Checker """

    username_entered = form.username.data
    password_entered = field.data

    # Check username is valid
    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or Password is incorrect")
    elif password_entered != user_object.password:
        raise ValidationError("Username or Password is incorrect")

class RegistrationForm(FlaskForm):
    """ Registration Form """

    username = StringField('username_label',
        validators=[InputRequired(message="Username Required"),
        Length(min=4, max=25, message="Do not meet the requirements")])
    password = PasswordField('password_label',
        validators=[InputRequired(message="Password Required"),
        Length(min=4, max=25, message="Do not meet the requirements")])
    confirm_pswd = PasswordField('confirm_pswd_label',
        validators=[InputRequired(message="Username Required"),
        EqualTo('password', message="Password Required")])
    submit_button = SubmitField('Create')

    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username has been taken")

class LoginForm(FlaskForm):
    """ Login Form """

    username = StringField('username_label', validators=[InputRequired(message="Username Required")])
    password = StringField('password_label', validators=[InputRequired(message="Password Required"), invalid_credentials])
    submit_button = SubmitField('Login')
