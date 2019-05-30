from api import db


class Photographers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(60), nullable=True)
    email = db.Column(db.String(60), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    timestamp = db.Column(db.String(30), unique=False, nullable=True)

    def __repr__(self):
        return f"Photographer('{self.fullName}', '{self.email}', '{self.phone}')"


db.create_all()
