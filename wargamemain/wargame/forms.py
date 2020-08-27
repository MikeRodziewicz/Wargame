from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class Question(FlaskForm):

    question_1 = RadioField(choices=[('1','1'),('2','2')], validators=[DataRequired()])
    question_2 = RadioField(choices=[('1','1'),('2','2')], validators=[DataRequired()])
    question_3 = RadioField(choices=[('1','1'),('2','2')], validators=[DataRequired()])
    submit = SubmitField("SUBMIT")



