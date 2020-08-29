from flask import render_template, Blueprint, session, redirect, url_for
from wargamemain.wargame.forms import Question
from wargamemain.wargame.backend import Character


game = Blueprint('game', __name__)

@game.route('/wargame', methods=['GET','POST'])
def wargame():

    form = Question()

    if form.validate_on_submit():
        session['question_1'] = form.question_1.data
        session['question_2'] = form.question_2.data
        session['question_3'] = form.question_3.data
        session['question_4'] = form.question_4.data
        session['question_5'] = form.question_5.data
        session['question_6'] = form.question_6.data
        session['question_7'] = form.question_7.data
        session['question_8'] = form.question_8.data
        session['question_9'] = form.question_9.data
        session['question_10'] = form.question_10.data
        session['question_11'] = form.question_11.data
        session['question_12'] = form.question_12.data
        session['question_13'] = form.question_13.data
        session['question_14'] = form.question_14.data
        session['question_15'] = form.question_15.data
        session['question_16'] = form.question_16.data
        session['question_17'] = form.question_17.data
        session['question_18'] = form.question_18.data
        session['question_19'] = form.question_19.data
        session['question_20'] = form.question_20.data
        session['question_21'] = form.question_21.data
        session['question_22'] = form.question_22.data
        session['question_23'] = form.question_23.data
        session['question_24'] = form.question_24.data
        return redirect(url_for('game.response'))

    return render_template('wargame.html', form=form)


@game.route('/response')
def response():
    answers_ei = [session['question_1'], session['question_2'], session['question_3'], session['question_4'],
                  session['question_5'], session['question_6']]
    answers_sn = [session['question_7'], session['question_8'], session['question_9'], session['question_10'],
                  session['question_11'], session['question_12']]
    answers_tf = [session['question_13'], session['question_14'], session['question_15'], session['question_16'],
                  session['question_17'], session['question_18']]
    answers_jp = [session['question_19'], session['question_20'], session['question_21'], session['question_22'],
                  session['question_23'], session['question_24']]
    char = Character()
    char.calculate_answers(answers_ei, 'EI')
    char.calculate_answers(answers_sn, 'SN')
    char.calculate_answers(answers_tf, 'TF')
    char.calculate_answers(answers_jp, 'JP')
    respo = char.personality
    return render_template(f'personalities/{respo}.html')




