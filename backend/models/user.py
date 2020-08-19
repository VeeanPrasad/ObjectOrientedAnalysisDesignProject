from backend.models.base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    from backend.db_manager import db

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password_digest = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, params):
        self.email = params.get('email')
        self.password_digest = params.get('password')

    @classmethod
    def is_admin_present(cls, params):
        data = cls.query.filter_by(email=params['email'], password_digest=params['password']).first()
        return True if data else False

    def create_or_update(self):
        data = User.query.filter_by(email=self.email, password_digest=self.password_digest).first()
        if data:
            return data
        else:
            return self.create()