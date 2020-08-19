from flask import Blueprint, request
from backend.services.game_services import create_game_service
from backend.helpers.flask_helper import flask_response, json_response

game_app = Blueprint('game_app', __name__)

@game_app.route('/game/create', methods=['POST'])
def quiz_create():
    try:
        data = create_game_service(request.data)
        response = json_response(data, status=200)
    except Exception as ex:
        response = json_response({'error': ex}, status=500)
    return response

