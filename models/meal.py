from database import db
from datetime import datetime

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_diet = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'datetime': self.datetime.isoformat() if self.datetime else None,
            'is_diet': self.is_diet 
        }