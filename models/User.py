# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
from app import db
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String)
    name = db.Column(db.String(190))
    password = db.Column(db.String(190))
    email = db.Column(db.String(190))
    phone = db.Column(db.String(190))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'phone': self.phone
        }