from flask import request, jsonify
from api.models import Photographers
from api import app, db


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
        me = Photographers(name, email, phone_number)
        db.session.add(me)
        db.session.commit()

        response = jsonify({
            "message": "User added successfully",
            "user_message": "User added successfully"
        }), 200

    return response


@app.route("/photographers")
def photographers():

    all_photographers = Photographers.query.all()
    new_photographers = []
    for photographer in all_photographers:
        new_photographers.append({
            "id": photographer.id,
            "fullName": photographer.fullName,
            "email": photographer.email,
            "phone": photographer.phone,
            "timestamp": photographer.timestamp
        })

    if not all_photographers:
        return jsonify({
            "message": "No data",
            "user_message": "There are no registered photographers"
        }), 200
    else:
        return jsonify(new_photographers), 200
