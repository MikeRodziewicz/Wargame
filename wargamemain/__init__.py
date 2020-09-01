from flask import Flask
from flask_mail import Mail

app = Flask(__name__)


app.config['SECRET_KEY'] = 'my_secret'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'xxx'
app.config["MAIL_PASSWORD"] = 'xxx'
mail = Mail(app)


from wargamemain.core.views import core
from wargamemain.promotion.views import promotion
from wargamemain.error_pages.handlers import error_pages
from wargamemain.wargame.views import game


app.register_blueprint(core)
app.register_blueprint(promotion)
app.register_blueprint(error_pages)
app.register_blueprint(game)


