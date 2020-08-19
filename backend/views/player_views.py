from flask import Blueprint,request
from backend.services.player_services import create_user_service, post_answer
from backend.helpers.flask_helper import json_response

player_app = Blueprint('player_app', __name__)

@player_app.route('/user/login', methods=['POST'])
def user_login():
    try:
        data = create_user_service(request.data)
        response = json_response(data, status=200)
    except Exception as ex:
        response = json_response({'error': ex}, status=500)
    return response


@player_app.route('/user/post_answer', methods=['POST'])
def view_quest():
    try:
        instance = post_answer(request.data)
        response = {'success': True, 'message': 'Player post successful', 'response': instance}
    except Exception as ex:
        response = {'failure': True, 'message': 'Player post failed', 'error': ex}
    return json_response(response)
