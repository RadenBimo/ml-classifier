# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

from app import db
class ModelProduct(db.Model):
    __tablename__ = 'model_product'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    model_id = db.Column(db.String)
    model_path = db.Column(db.String)
    score = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'model_id': self.model_id,
            'model_path': self.model_path,
            'score': self.score,
            'product_id': self.product_id,
        }
    
    def __repr__(self):
        return f"<TrainingData(client_id={self.client_id}, message='{self.message}', category='{self.category}')>"