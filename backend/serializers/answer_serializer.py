from backend.serializers.base_serializer import ma
from backend.models.answer import Answer

class AnswerSchema(ma.ModelSchema):
    class Meta:
        model = Answer

answer_schema = AnswerSchema()