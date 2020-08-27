from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret'


from wargamemain.core.views import core
from wargamemain.promotion.views import promotion
from wargamemain.error_pages.handlers import error_pages
from wargamemain.wargame.views import game


app.register_blueprint(core)
app.register_blueprint(promotion)
app.register_blueprint(error_pages)
app.register_blueprint(game)


