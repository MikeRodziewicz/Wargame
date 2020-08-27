from flask import render_template, Blueprint, session, redirect, url_for
from wargamemain.wargame.forms import Question


game = Blueprint('game', __name__)

@game.route('/wargame', methods=['GET','POST'])
def wargame():
    form = Question()

    if form.validate_on_submit():
        session['question_1'] = form.question_1.data
        session['question_2'] = form.question_2.data
        session['question_3'] = form.question_3.data

        return redirect(url_for('game.response'))

    return render_template('wargame.html', form=form)


@game.route('/response')
def response():
    if session['question_1'] == '2':
        odp = 'Pirat'
        return render_template('response.html', odp=odp)
    else:
        odp = 'dziad'
        return render_template('response.html', odp=odp)

