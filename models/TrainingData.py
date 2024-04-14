from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TrainingData(db.Model):
    __tablename__ = 'training_datas'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    category = db.Column(db.String)
    client_id = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'message': self.message,
            'category': self.category,
            'client_id': self.client_id,
        }