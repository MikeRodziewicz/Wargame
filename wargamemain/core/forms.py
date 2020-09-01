from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(),Email()])
    title = StringField('Title', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField("Contact Us")

