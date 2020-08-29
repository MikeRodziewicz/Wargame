from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired


class Question(FlaskForm):

    question_1 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_2 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_3 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_4 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_5 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_6 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_7 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_8 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_9 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_10 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_11 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_12 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_13 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_14 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_15 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_16 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_17 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_18 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_19 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_20 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_21 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_22 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_23 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    question_24 = RadioField(choices=[1, 2, 3, 4, 5, 6], validators=[DataRequired()])
    submit = SubmitField("SUBMIT")



