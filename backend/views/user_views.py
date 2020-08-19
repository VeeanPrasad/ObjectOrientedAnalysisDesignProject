from backend.views import view_app
from backend.services.user_services import create_admin, admin_login
from backend.helpers.flask_helper import json_response
from flask import Blueprint, request

user_app = Blueprint('user_app', __name__)

@user_app.route('/users/create', methods=['POST'])
def admin_register_view():
    try:
        data = create_admin(request.data)
        response = json_response(data, status=200)
    except Exception as ex:
        response = json_response({'error': ex}, status=500)
    return response

@user_app.route('/quizzes/user_token', methods=['POST'])
def admin_login_view():
    try:
        data = admin_login(request.data)
        if data['jwt']:
            response = json_response(data, status=200)
        else:
            response = json_response({'message': 'Wrong credentials'}, status=404)
    except Exception as ex:
        response = json_response({'message': 'Wrong credentials'}, status=404)
        # response = {'failure': True, 'message': "admin login failed", 'error': ex}
    # return flask_response(response)
    return response

@user_app.route('/')
def hello():
    return "Hello World"


