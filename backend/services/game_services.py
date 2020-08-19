from backend.helpers.flask_helper import convert
from backend.models import game
from backend.helpers.redis_client import r
from backend.services.base_services import Handler
from backend.serializers.game_serializer import game_schema

class ParamParser(Handler):

    def handle_request(self, **kwargs):
        parsed_params = convert(kwargs['requestData'])
        if self._successor is not None:
            return self._successor.handle_request(parsedParams=parsed_params)


class CreateGame(Handler):

    def handle_request(self, **kwargs):
        game_obj = game.Game(kwargs['parsedParams'])
        response = game_obj.create_or_update()

        if self._successor is not None:
            return self._successor.handle_request(response=response)


class RedisUpdater(Handler):

    def handle_request(self, **kwargs):
        if 'response' in kwargs:
            redis_write_score(kwargs['response'])
            return game_schema.dump(kwargs['response'])

def create_game_service(request_data):
    handler_1 = RedisUpdater()
    handler_2 = CreateGame(handler_1)
    handler_3 = ParamParser(handler_2)
    response = handler_3.handle_request(requestData=request_data)
    return response

def redis_write_score(instance):
    r.set(instance.title, instance.quiz_id)
