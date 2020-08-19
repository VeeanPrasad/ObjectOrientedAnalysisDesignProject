from backend.models.base import BaseModel
from sqlalchemy.types import Boolean

class Player(BaseModel):
    __tablename__ = 'players'

    from backend.db_manager import db

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String())
    entered_answer = db.Column(Boolean)
    game_id = db.Column(db.Integer())
    streak = db.Column(db.Integer())
    last_correct = db.Column(Boolean)
    answer = db.Column(db.String())
    score = db.Column(db.Integer(), default=0)


    def __init__(self, params):
        self.id = params.get('id', None)
        self.nickname = params.get('name')
        self.game_id = params.get('gameId')
        self.score = params.get('score', 0)

    def create_or_update(self):
        data = Player.query.filter_by(nickname=self.nickname).first()
        if data:
            return data
        else:
            return self.create()






