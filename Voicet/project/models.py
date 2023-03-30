from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    posts = db.relationship('Videos',backref='user', lazy=True)

class Videos(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    youtube_url = db.Column(db.String(200), nullable=True)
    file_name = db.Column(db.String(200), nullable=True)
    file_extension = db.Column(db.String(10) )
    file_path = db.Column(db.String(200))
    original_filename = db.Column(db.String(200))
    random_filename = db.Column(db.String(200))
    translate_to_languge = db.Column(db.String(200))
    translate_to_gender = db.Column(db.String(200))
    video_processed = db.Column(db.Integer)
    percent_processed = db.Column(db.Integer)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    posted_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
