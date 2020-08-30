from flask import render_template, Blueprint, session
from wargamemain.promotion.forms import ContactForm
from wargamemain.promotion.contact import Message


promotion = Blueprint('promotion', __name__)

@promotion.route('/about', methods = ['GET', 'POST'])
def about():
    form = ContactForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['title'] = form.title.data
        session['message'] = form.message.data
        sending = Message(session['name'], session['email'], session['title'], session['message'])
        sending.sending_email()

    return render_template('about.html', form=form)