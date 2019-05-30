from flask import request, jsonify
from api.models import Photographers
from api import app


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
