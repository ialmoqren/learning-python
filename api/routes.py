from flask import request, jsonify
from api.models import Photographers, Orders, Users
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


@app.route("/orders")
def orders():

    all_orders = Orders.query.all()
    new_orders = []
    for order in all_orders:
        new_orders.append({
            "id": order.id,
            "fullName": order.fullName,
            "email": order.email,
            "phone": order.phone,
            "details": order.details,
            "timestamp": order.timestamp
        })

    if not all_orders:
        return jsonify({
            "message": "No data",
            "user_message": "There are no orders"
        }), 200
    else:
        return jsonify(new_orders), 200
