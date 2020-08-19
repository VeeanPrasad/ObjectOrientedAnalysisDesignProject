from backend import config
from flask import Flask
from flask_cors import CORS

# Decorator pattern:
# This pattern creates a decorator class which wraps the original class and providing and adding CORS headers to the api responses

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app

app = create_app()

#Decorator for adding CORS headers to the api responses
CORS(app)
