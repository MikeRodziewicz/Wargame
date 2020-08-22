from flask import render_template, Blueprint
from wargamemain.wargame.forms import Answer
from wargamemain import db

questions = db.Table('import_test', db.metadata, autoload=True, autoload_with=db.engine)
game = Blueprint('game', __name__)


@game.route('/wargame', methods=['GET','POST'])
def wargame():
    form = Answer()
    results = db.session.query(questions).where()
    return render_template('wargame.html', results=results, form=form)