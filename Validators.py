from wtforms import StringField, SubmitField, Form, PasswordField
from wtforms import validators


class LoginForm(Form):
    id = StringField('UserName', [validators.DataRequired('Please enter your name.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Login')


class RegisterForm(Form):
    id = StringField('UserName', [validators.DataRequired('Please enter your name.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Register')