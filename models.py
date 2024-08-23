from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User>: {self.id} - {self.username}'
    

class FreshiiData(db.Model):
    __tablename__ = 'freshii_data'
    
    date = db.Column(db.Date, unique=True, nullable=False, primary_key=True)
    c1 = db.Column(db.Integer, nullable=False, default=0)
    c5 = db.Column(db.Integer, nullable=False, default=0)
    c10 = db.Column(db.Integer, nullable=False, default=0)
    c25 = db.Column(db.Integer, nullable=False, default=0)
    c50 = db.Column(db.Integer, nullable=False, default=0)
    d1 = db.Column(db.Integer, nullable=False, default=0)
    d2 = db.Column(db.Integer, nullable=False, default=0)
    d5 = db.Column(db.Integer, nullable=False, default=0)
    d10 = db.Column(db.Integer, nullable=False, default=0)
    d20 = db.Column(db.Integer, nullable=False, default=0)
    d50 = db.Column(db.Integer, nullable=False, default=0)
    d100 = db.Column(db.Integer, nullable=False, default=0)
    total_value = db.Column(db.Float, nullable=False, default=0)
    rolls = db.Column(db.Float, nullable=False, default=0)
    float_value = db.Column(db.Float, nullable=False, default=150)
    cash_drop = db.Column(db.Float, nullable=False, default=0)
    entered_by = db.Column(db.String(255), nullable=False)
