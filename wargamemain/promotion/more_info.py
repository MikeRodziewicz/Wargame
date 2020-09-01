from flask_mail import Message
from wargamemain import mail, app



class Email(Message):

    body = '''As you requested, please find additional information in our short document attached.'''

    def __init__(self, email):
        self.email = email


    def sending_email(self):
        msg = Message("TYClasses Info Request", sender='xxx', recipients=[self.email], body=self.body)
        with app.open_resource('static/token_1.png') as fp:
            msg.attach('token_1.png', 'token_1/png', fp.read())
        mail.send(msg)