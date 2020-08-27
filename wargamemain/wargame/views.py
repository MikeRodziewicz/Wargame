from flask import render_template, Blueprint
from wargamemain.wargame.forms import Question


game = Blueprint('game', __name__)

@game.route('/wargame', methods=['GET','POST'])
def wargame():

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


    return render_template('response.html', form=form, odp=odp)