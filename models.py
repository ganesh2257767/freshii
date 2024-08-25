from app import db, bcrypt
from flask_login import UserMixin
from sqlalchemy import event
from flask_admin.contrib.sqla import ModelView
# from flask_login import current_user

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    role = db.Column(db.String(255), nullable=False)
    # freshii_data = db.relationship('FreshiiData', backref=db.backref('user'))
    

    def __repr__(self):
        return self.username
    

class FreshiiData(db.Model):
    __tablename__ = 'freshii_data'
    
    date = db.Column(db.Date, primary_key=True, nullable=False, unique=True)
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
    entered_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    entered_by_user = db.relationship('User', foreign_keys=[entered_by_user_id])
    updated_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    updated_by_user = db.relationship('User', foreign_keys=[updated_by_user_id])

class RestrictedAdminView(ModelView):
    def is_accessible(self):
        from routes import current_user
        return current_user.is_authenticated and current_user.role == "admin"

@event.listens_for(User.password, "set", retval=True)
def hash_password(target, value, oldvalue, initiator):
    if value != oldvalue and value is not None:
        return bcrypt.generate_password_hash(value).decode("utf-8")
    return value