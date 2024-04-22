from sqlalchemy.dialects.mysql import LONGTEXT
from app import db

class TrainingData(db.Model):
    __tablename__ = 'training_datas'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(LONGTEXT)
    category = db.Column(db.String(100))
    client_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'message': self.message,
            'category': self.category,
            'client_id': self.client_id,
            'product_id': self.product_id
        }
    
    def __repr__(self):
        return f"<TrainingData(client_id={self.client_id}, message='{self.message}', category='{self.category}')>"