#models.py
from doctorblog import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    license_key=db.Column(db.String(128))
    posts = db.relationship('Medicine',backref='author',lazy=True)

    def __init__(self,email,username,password,license_key):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.license_key=license_key

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username {self.username}"


class Medicine(db.Model):

    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    patient_name = db.Column(db.String(140),nullable=False)
    medicine = db.Column(db.Text,nullable=False)
    description=db.Column(db.Text,nullable=False)
    allergy=db.Column(db.Text,nullable=False)
    timing=db.Column(db.Text,nullable=False)

    def __init__(self,patient_name,medicine,user_id,description,allergy,
                                timing):
        self.patient_name=patient_name
        self.medicine=medicine
        self.user_id = user_id
        self.description=description
        self.allergy=allergy
        self.timing=timing
        

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.patient_name}"
