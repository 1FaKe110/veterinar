# app/models.py
from app import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description_short = db.Column(db.Text)
    description_full = db.Column(db.Text)
    image_url = db.Column(db.Text)

    def __repr__(self):
        return f"Service('{self.title}')"
