from backend.helpers.flask_helper import convert
from backend.models import question
from backend.models.quiz import Quiz
from backend.helpers.redis_client import r

REDIS_SEPARATOR='#~#'

def create_question_services(request_data):
    params = convert(request_data)
    ques_obj = question.Question(params)
    quiz = Quiz(params['quiz']) if 'quiz' in params else Quiz.query.filter_by(id=ques_obj.quiz_id).first()
    if quiz: ques_obj.quiz = quiz
    response = ques_obj.create_or_update()
    if response: return response.__dict__

def get_stats(quiz_id, question_id):
    response = {}
    for option in range(1,5):
        key = REDIS_SEPARATOR.join([str(quiz_id), str(question_id), str(option)])
        current_val = r.get(key)
        response["{}".format(option)] = int(current_val.decode("utf-8")) if current_val else 0
    return response