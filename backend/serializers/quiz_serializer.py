from backend.serializers.base_serializer import ma
from backend.models.quiz import Quiz
from marshmallow import fields
from backend.serializers.question_serializer import QuestionSchema

class QuizSchema(ma.ModelSchema):
    questions = fields.List(fields.Nested(QuestionSchema))
    class Meta:
        model = Quiz

quiz_schema = QuizSchema(many=True)