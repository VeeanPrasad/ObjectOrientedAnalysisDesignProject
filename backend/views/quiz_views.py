from flask import Blueprint, request
from backend.services.quiz_services import create_quiz_services, get_all
from backend.helpers.flask_helper import flask_response, json_response

quiz_app = Blueprint('quiz_app', __name__)

@quiz_app.route('/quiz/create', methods=['POST'])
def quiz_create():
    try:
        instance = create_quiz_services(request.data)
        response = {'success': True, 'message': 'quiz creation success', 'response': instance}
    except Exception as ex:
        response = {'success': False, 'message': 'quiz creation failed', 'error': ex}
    return flask_response(response)

@quiz_app.route('/quizzes/list', methods=['GET'])
def view_quiz():
    try:
        data = get_all()
        response = json_response(data, status=200)
    except Exception as ex:
        response = json_response({'error': ex}, status=500)
    return response


