from flask_security.forms import LoginForm, RegisterForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class ExtendedLoginForm(LoginForm):
    email = StringField('Benutzername', validators=[DataRequired()])


class ExtendedRegisterForm(RegisterForm):
    username = StringField('Benutzername', validators=[DataRequired()])
