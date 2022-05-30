from dataclasses import Field
import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from BlogWall.models import User

class LoginForm(FlaskForm):
    style={'class': 'btn btn-primary'}
    email = StringField('Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Enter Email"})
    password = PasswordField('Password', validators=[DataRequired()],render_kw={"placeholder": "Enter Password"})
    submit = SubmitField('Login',render_kw=style)


class RegistrationForm(FlaskForm):
    style={'class': 'btn btn-primary'}
    email = StringField('Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "Enter Email"})
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "Enter Username"})
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm',message='Passwords must match!')],render_kw={"placeholder": "Enter Password"})
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()],render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Register',render_kw=style)


    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')


    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This Username Already Exists!')


class UpdateUserForm(FlaskForm):
    style={'class': 'btn btn-primary'}
    email = StringField('Email', validators=[DataRequired(), Email()],render_kw={"placeholder": "New Email"})
    username = StringField('Username', validators=[DataRequired()],render_kw={"placeholder": "New Username"})
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Update',render_kw=style)

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')


    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This Username Already Exists!')
