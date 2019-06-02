from flask import request, jsonify
from api.schemas.photographers_schema import photographers_schema
from api.schemas.orders_schema import orders_schema
from api.models.photographers import Photographers
from api.models.orders import Orders
from api.models.users import Users
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

    if not name or not email or not phone_number:
        response = jsonify({
            "message": "Empty data received",
            "user_message": "Please fill all the info"
        }), 400
    else:
        new_photographer = Photographers(name, email, phone_number)
        db.session.add(new_photographer)
        db.session.commit()

        response = jsonify({
            "message": "Photographer added successfully",
            "user_message": "Photographer added successfully"
        }), 200

    return response


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        response = jsonify({
            "message": "Empty data received",
            "user_message": "Please fill all the info"
        }), 400
    else:
        user = Users.query.filter_by(username=username).first()

        if user is None or user.password != password:
            response = jsonify({
                "message": "Email or password is not correct",
                "user_message": "Email or password is not correct"
            }), 401
        else:
            response = jsonify({
                "message": "User logged in successfully",
                "user_message": "User logged in successfully"
            }), 200

    return response


@app.route("/order", methods=["POST"])
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


@app.route("/photographers")
def photographers():

    all_photographers = Photographers.query.all()

    if not all_photographers:
        return jsonify({
            "message": "No data",
            "user_message": "There are no registered photographers"
        }), 200
    else:
        return photographers_schema.jsonify(all_photographers), 200


@app.route("/orders")
def orders():

    all_orders = Orders.query.all()

    if not all_orders:
        return jsonify({
            "message": "No data",
            "user_message": "There are no orders"
        }), 200
    else:
        return orders_schema.jsonify(all_orders), 200
