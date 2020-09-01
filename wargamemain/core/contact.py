from flask_mail import Message
from wargamemain import mail, app



class Email(Message):

    def __init__(self, name, email, title, message):
        self.name = name
        self.email = email
        self.title = title
        self.message = message

    def sending_email(self):
        msg = Message(self.title, sender='xxx', recipients=['xxx'], cc=[self.email], body=self.message)
        with app.open_resource('static/token_1.png') as fp:
            msg.attach('token_1.png', 'token_1/png', fp.read())
        mail.send(msg)
