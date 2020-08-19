from backend.serializers.base_serializer import ma
from backend.models.game import Game
from marshmallow import fields
from backend.serializers.quiz_serializer import QuizSchema

# Chain of responsibility pattern is used to here
# to achieve loose coupling in software design where the responsibility was passed among
# param parser,game creater and redis updater where the object in the chain will decide the the sequence 
# processing the request.

class GameSchema(ma.ModelSchema):
    quiz = fields.List(fields.Nested(QuizSchema))
    class Meta:
        model = Game

game_schema = GameSchema()
