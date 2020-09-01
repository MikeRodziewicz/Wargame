from flask import render_template, Blueprint, session, url_for, redirect
from wargamemain.core.contact import Email
from wargamemain.core.forms import ContactForm



core = Blueprint('core', __name__)


@core.route('/')
def index():

    return render_template('index.html')


@core.route('/info', methods = ['GET', 'POST'])
def info():
    form = ContactForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['title'] = form.title.data
        session['message'] = form.message.data
        sending = Email(session['name'], session['email'], session['title'], session['message'])
        sending.sending_email()
        return redirect(url_for('core.thankyou'))


    return render_template('contact.html', form=form)


@core.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
