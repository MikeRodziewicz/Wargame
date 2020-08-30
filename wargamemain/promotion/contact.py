import smtplib
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class Message(object):

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

    
