from flask import request, jsonify
from api.models.photographers import Photographers
from api import app, db


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone_number = data.get("phone_number")

    if not name or not email or not phone_number:
        response = jsonify({
            "message": "Empty data received",
            "user_message": "Please fill all the info"
        }), 400
    else:
        new_photographer = Photographers(name, email, phone_number)
        # TODO: Maybe use Photographer.add instead of db.session.add?
        db.session.add(new_photographer)
        db.session.commit()

        response = jsonify({
            "message": "Photographer added successfully",
            "user_message": "Photographer added successfully"
        }), 200

    return response
