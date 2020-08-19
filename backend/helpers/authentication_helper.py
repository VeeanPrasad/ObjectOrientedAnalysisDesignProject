import jwt

def encode(params):
    auth_dict = {'email': params['email'], 'password': params['password']}
    byte_data = jwt.encode(auth_dict, 'secret', algorithm='HS256')
    return byte_data.decode('utf-8')

def decode(params):
    token = params['token'].encode('utf-8')
    return jwt.decode(token, 'secret', algorithm='HS256')
