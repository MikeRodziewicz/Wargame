from flask_wtf import FlaskForm
from wtforms import RadioField
from wtforms.validators import DataRequired

class Answer(FlaskForm):
    response = RadioField(choices=['1','2'],validators=[DataRequired()])