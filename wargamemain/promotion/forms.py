from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, Email

class PromotionForm(FlaskForm):

    email = StringField('E-mail', validators=[DataRequired(),Email()])
    submit = SubmitField("Request Info")
