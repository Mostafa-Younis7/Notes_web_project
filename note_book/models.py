from . import db, login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    data = db.Column(db.String(3000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user = db.Column(db.Integer(), db.ForeignKey('user.id'))

    
