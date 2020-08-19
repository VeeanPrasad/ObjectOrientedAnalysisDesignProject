from backend.serializers.base_serializer import ma
from backend.models.player import Player
from marshmallow import fields


# Chain of responsibility pattern is used to here
# to achieveloose coupling in software design where the responsibility was passed among
# paramparser,player creater and redis updater where the object in the chain will decide the the sequence 
# processing the request.

class PlayerSchema(ma.ModelSchema):
    answers = fields.List(fields.Nested("AnswerSchema"))
    class Meta:
        model = Player

player_schema = PlayerSchema()
