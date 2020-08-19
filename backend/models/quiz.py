from backend.models.base import BaseModel
from sqlalchemy.types import Boolean
from backend.db_manager import db

class Quiz(BaseModel):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String())
    difficulty = db.Column(db.String())

    def __init__(self, params):
        self.id = params.get('id', None)
        self.category = params.get('category')
        self.difficulty = params.get('difficulty')

    def create_or_update(self):
        if self.id:
            data = Quiz.query.filter_by(id=self.id).first()
            if data:
                return data
        self.create()
        return Quiz.query.order_by(Quiz.created_on.desc()).first()

class Question(BaseModel):
    __tablename__ = 'questions'

    from backend.db_manager import db

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    quiz_id = db.Column(db.Integer(), db.ForeignKey(Quiz.id))


    # def __init__(self, params):
    #     self.content = params.get('content', None)

    def create_or_update(self):
        if self.id:
            data = Question.query.filter_by(id=self.id).first()
            if data:
                return data
        return self.create()

Quiz.questions = db.relationship(Question, backref="quiz")
#
# class Answer(BaseModel):
#     __tablename__ = 'answers'
#
#     id = db.Column(db.Integer, primary_key=True)
#     answer = db.Column(db.String())
#     correct = db.Column(Boolean)
#     question_id = db.Column(db.Integer(), db.ForeignKey(Question.id))
#
# Question.answers = db.relationship(Answer, backref="question")














