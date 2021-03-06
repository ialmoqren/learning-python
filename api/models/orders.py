from api import db
from datetime import datetime


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(60))
    email = db.Column(db.String(60))
    phone = db.Column(db.String(20))
    details = db.Column(db.String(2000))
    timestamp = db.Column(db.String(30), nullable=False,
                          default=f"{datetime.now():%m/%d/%y %I:%M %p}")

    def __init__(self, fullName, email, phone, details):
        self.fullName = fullName
        self.email = email
        self.phone = phone
        self.details = details

    def __repr__(self):
        return f"Order('{self.fullName}', '{self.email}', '{self.phone}')"
