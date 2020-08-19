from flask import Flask

app = Flask(__name__)

from wargamemain.core.views import core
from wargamemain.promotion.views import promotion
from wargamemain.error_pages.handlers import error_pages
from wargamemain.wargame.views import game


app.register_blueprint(core)
app.register_blueprint(promotion)
app.register_blueprint(error_pages)
app.register_blueprint(game)