from flask import render_template, Blueprint, request


game = Blueprint('game', __name__)


questions = {'1':'pytanie pierwsze', '2':'pytanie drugie', '3':'Pytanie trzecie'}

@game.route('/wargame', methods=['GET','POST'])
def wargame():
    for i in questions.keys():
        q = questions[i]
    return render_template('wargame.html', q=q)