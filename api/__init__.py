from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

# Getting the DB parameters from the .env file
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PWD = os.getenv('MYSQL_PWD')
MYSQL_DB = os.getenv('MYSQL_DB')
print(f"db parameters: {MYSQL_HOST} {MYSQL_USER} {MYSQL_PWD} {MYSQL_DB}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}:3306/{MYSQL_DB}'
db = SQLAlchemy(app)


class Photographers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(60), nullable=True)
    email = db.Column(db.String(60), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    timestamp = db.Column(db.String(30), unique=False, nullable=True)

    def __repr__(self):
        return f"Photographer('{self.fullName}', '{self.email}', '{self.phone}')"


db.create_all()


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone_number = data.get("phone_number")

    print(name, email, phone_number)

    if not name or not email or not phone_number:
        response = jsonify({
            "message": "Empty data received",
            "user_message": "Please fill all the info"
        }), 400
    else:
        response = jsonify({
            "name": name,
            "email": email,
            "phone_number": phone_number
        }), 200

    return response


@app.route("/photographers")
def photographers():

    allPhotographers = Photographers.query.all()
    newPhotographers = []
    for photographer in allPhotographers:
        newPhotographers.append({
            "id": photographer.id,
            "fullName": photographer.fullName,
            "email": photographer.email,
            "phone": photographer.phone,
            "timestamp": photographer.timestamp
        })

    if not allPhotographers:
        return jsonify({
            "message": "No data",
            "user_message": "There are no registered photographers"
        }), 200
    else:
        return jsonify(newPhotographers), 200
