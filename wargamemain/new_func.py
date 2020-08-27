from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret'


class Question(FlaskForm):
    question_1 = RadioField(choices=[1,2,3,4,5,6], validators=[DataRequired()])
    question_2 = RadioField(choices=[1,2,3,4,5,6], validators=[DataRequired()])
    question_3 = RadioField(choices=[1,2,3,4,5,6], validators=[DataRequired()])
    submit = SubmitField("SUBMIT")


@app.route('/', methods=['GET','POST'])
def index():

    form = Question()

    if form.validate_on_submit():
        session['question_1'] = form.question_1.data
        session['question_2'] = form.question_2.data
        session['question_3'] = form.question_3.data

        return redirect(url_for('index'))

    return render_template('new.html', form=form)

def func(item):
    foo = int(item)
    return foo


@app.route('/thankyou')
def thankyou():
    odp_1= type(func(session['question_1']))
    odp = type(session['question_1'])
    return render_template('thankyou.html', odp=odp, odp_1=odp_1)

if __name__ == '__main__':
    app.run()