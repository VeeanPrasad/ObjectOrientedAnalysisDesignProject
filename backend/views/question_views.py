from flask import Blueprint, request
from backend.services.question_services import create_question_services, get_stats
from backend.helpers.flask_helper import flask_response

question_app = Blueprint('question_app', __name__)

@question_app.route('/question/create', methods=['POST'])
def question_create():
    try:
        instance = create_question_services(request.data)
        response = {'success': True, 'message': 'question creation success', 'response': instance}
    except Exception as ex:
        response = {'success': False, 'message': 'question creation failed', 'error': ex}
    return flask_response(response)

@question_app.route('/question/stats/<quiz_id>/<question_id>', methods=['GET'])
def get_stats_view(quiz_id, question_id):
    try:
        instance = get_stats(quiz_id, question_id)
        response = {'success': True, 'message': 'Get question stats successful', 'response': instance}
    except Exception as ex:
        response = {'failure': True, 'message': 'Get question stats failed', 'error': ex}
    return flask_response(response)