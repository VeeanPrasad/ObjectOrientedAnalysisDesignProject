from flask_marshmallow import Marshmallow
from flask import Flask

new_app = Flask(__name__)

ma = Marshmallow(new_app)