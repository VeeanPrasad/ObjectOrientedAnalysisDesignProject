from backend.helpers.flask_helper import convert
from backend.models import player
from backend.helpers.redis_client import r
from backend.services.base_services import Handler
from backend.serializers.player_serializer import player_schema

REDIS_SEPARATOR='#~#'

class ParamParser(Handler):

    def handle_request(self, **kwargs):
        parsed_params = convert(kwargs['requestData'])
        if self._successor is not None:
            return self._successor.handle_request(parsedParams=parsed_params)


class CreatePlayer(Handler):

    def handle_request(self, **kwargs):
        user_obj = player.Player(kwargs['parsedParams'])
        response = user_obj.create_or_update()

        if self._successor is not None:
            return self._successor.handle_request(response=response)


class RedisUpdater(Handler):

    def handle_request(self, **kwargs):
        if 'response' in kwargs:
            redis_write_score(kwargs['response'])
            return player_schema.dump(kwargs['response'])

def create_user_service(request_data):
    handler_1 = RedisUpdater()
    handler_2 = CreatePlayer(handler_1)
    handler_3 = ParamParser(handler_2)
    response = handler_3.handle_request(requestData=request_data)
    return response

def redis_write_score(player):
    redis_key = REDIS_SEPARATOR.join([player.nickname, str(player.game_id)])
    r.set(redis_key, player.score)

def post_answer(request_data):
    params = convert(request_data)
    user_obj = player.Player(params)
    if 'answerParams' in params:
        answer_params = params['answerParams']
        if answer_params['selectedOption'] == answer_params['correctOption']:
            user_obj.score += 1

    response = user_obj.create_or_update()
    return response.__dict__

def redis_write_option_count(quiz_id, question_id, option):
    key = REDIS_SEPARATOR.join([quiz_id, question_id, option])
    current_val = r.get(key)
    if current_val:
        current_val = int(current_val.decode("utf-8"))
        r.set(key, current_val+1)
    else:
        r.set(key, 1)

