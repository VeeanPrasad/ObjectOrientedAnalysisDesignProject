from backend.helpers.flask_helper import convert
from backend.models import quiz
from backend.models.user import User
from backend.serializers import quiz_serializer

def create_quiz_services(request_data):
    params = convert(request_data)
    quiz_obj = quiz.Quiz(params)
    if 'questions' in params:
        questions = [quiz.Question(param) for param in params]
    else:
        questions = quiz.Question.query.filter_by(quiz_id=quiz_obj.id).all()
    if questions: quiz_obj.questions = questions
    if 'admin' in params:
        admin = User(params['admin'])
    else:
        admin = User.query.filter_by(id=quiz_obj.created_by).first()
    if admin: quiz_obj.admin = admin
    response = quiz_obj.create_or_update()
    if response: return response.__dict__

def get_all():
    data = quiz.Quiz.query.all()
    return quiz_serializer.quiz_schema.dump(data)