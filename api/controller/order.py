from flask import request, jsonify, Blueprint
from api import db
from api.models.orders import Orders

api = Blueprint('order_api', __name__)


@api.route("/order", methods=["POST"])
def order():

    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone_number = data.get("phone_number")
    details = data.get("details")

    print(name, email, phone_number, details)

    if not name or not email or not phone_number or not details:
        response = jsonify({
            "message": "Empty data received",
            "user_message": "Please fill all the info"
        }), 400
    else:
        new_order = Orders(name, email, phone_number, details)
        db.session.add(new_order)
        db.session.commit()

        response = jsonify({
            "message": "Order added successfully",
            "user_message": "Order added successfully"
        }), 200

    return response
