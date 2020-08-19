from backend.helpers.flask_helper import convert
from backend.models import user
from backend.helpers.authentication_helper import encode

def admin_login(request_data):
    token = None
    params = convert(request_data)
    if user.User.is_admin_present(params['auth']):
        token = encode(params['auth'])
    return {"jwt": token}

def create_admin(request_data):
    params = convert(request_data)
    # {"email": "janani483@gmail.com", "password": "lol", "password_confirmation": "lol"}
    admin_obj = user.User(params)
    response = admin_obj.create_or_update()
    return response.__dict__