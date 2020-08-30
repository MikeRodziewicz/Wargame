import smtplib


class Message(object):

    def __init__(self, name, email, title, message):
        self.name = name
        self.email = email
        self.title = title
        self.message = message

    def sending_email(self):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("email", "psw")
            subject = self.title
            cc = self.email
            msg = f'{subject}/n/n{cc} wrote: {self.message}'
            smtp.sendmail("email", "email", msg)
