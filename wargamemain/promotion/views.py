from flask import render_template, Blueprint


promotion = Blueprint('promotion', __name__)

@promotion.route('/about')
def about():

    return render_template('about.html')