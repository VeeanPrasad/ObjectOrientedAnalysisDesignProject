from backend.models.base import BaseModel
from backend.models.quiz import Quiz
from backend.db_manager import db
from backend.models.pin_generator import PinGenerator

class Game(BaseModel):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    quiz_id = db.Column(db.Integer(), db.ForeignKey(Quiz.id))

    def __init__(self, params):
        self.id = params.get('id', None)
        self.title = params.get('title')
        self.quiz_id = params.get('quizId')
        if self.title is None:
            pin_generator = PinGenerator()
            self.title = pin_generator.generate_pin()

    def create_or_update(self):
        data = Game.query.filter_by(id=self.id).first()
        if data:
            return data
        else:
            return self.create()

Game.quiz = db.relationship(Quiz, backref="game")

