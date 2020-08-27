from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret'


class Question(FlaskForm):

    question_1 = RadioField(choices=[('1','1'),('2','2')], validators=[DataRequired()])
    question_2 = RadioField(choices=[('1','1'),('2','2')], validators=[DataRequired()])
    question_3 = RadioField(choices=[('1','1'),('2','2')], validators=[DataRequired()])
    submit = SubmitField("SUBMIT")



@app.route('/', methods=['GET','POST'])
def index():

    question_1 = None
    question_2 = None
    question_3 = None
    odp = None
    form = Question()

    if form.validate_on_submit():
        question_1 = form.question_1.data
        odp = responses(question_1)
        form.question_1.data = ''

        question_2 = form.question_2.data
        question_3 = form.question_3.data

        form.question_2.data = None
        form.question_3.data = None
    else:
        flash("uzupelnij wszystkie pola")


    return render_template('new.html', form=form, odp=odp)


if __name__ == '__main__':
    app.run()