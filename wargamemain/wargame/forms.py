from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired
from wargamemain.wargame.backend import list_of_questions, list_of_answers

questions = {'q1':'bla bla bla'}

class Question(FlaskForm):

    question_1 = RadioField(questions['q1'], choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_2 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_3 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_4 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_5 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_6 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_7 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_8 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_9 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_10 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_11 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_12 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_13 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_14 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_15 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_16 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_17 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_18 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_19 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_20 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_21 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_22 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_23 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    question_24 = RadioField(questions['q1'],choices=[list_of_answers[0],list_of_answers[1],list_of_answers[2],list_of_answers[3]], validators=[DataRequired()])
    submit = SubmitField("SUBMIT")



