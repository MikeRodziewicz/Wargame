from flask import render_template, Blueprint, session, flash, redirect, url_for
from wargamemain.promotion.forms import PromotionForm
from wargamemain.promotion.more_info import Email


promotion = Blueprint('promotion', __name__)

@promotion.route('/about', methods = ['GET', 'POST'])
def about():

    form = PromotionForm()

    if form.validate_on_submit():
        session['email'] = form.email.data
        sending = Email(session['email'])
        sending.sending_email()
        flash("check your e-mail!")
        return redirect(url_for('promotion.about'))

    return render_template('about.html', form=form)
