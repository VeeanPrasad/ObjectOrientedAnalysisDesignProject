from backend.models.base import BaseModel
from sqlalchemy.types import Boolean
from backend.db_manager import db
from backend.models.quiz import Question

class Answer(BaseModel):
    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String())
    correct = db.Column(Boolean)
    question_id = db.Column(db.Integer(), db.ForeignKey(Question.id))

Question.answers = db.relationship(Answer, backref="question")
