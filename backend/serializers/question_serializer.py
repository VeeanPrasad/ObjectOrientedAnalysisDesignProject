from backend.serializers.base_serializer import ma
from backend.models.quiz import Question
from marshmallow import fields
from backend.serializers.answer_serializer import AnswerSchema

class QuestionSchema(ma.ModelSchema):
    answers = fields.List(fields.Nested(AnswerSchema))
    class Meta:
        model = Question

question_schema = QuestionSchema(many=True)