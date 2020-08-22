from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='#',pw='#',url='127.0.0.1:5432',db='wargame_test')

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SECRET_KEY'] = 'my_secret'

db = SQLAlchemy(app)




from wargamemain.core.views import core
from wargamemain.promotion.views import promotion
from wargamemain.error_pages.handlers import error_pages
from wargamemain.wargame.views import game


app.register_blueprint(core)
app.register_blueprint(promotion)
app.register_blueprint(error_pages)
app.register_blueprint(game)


