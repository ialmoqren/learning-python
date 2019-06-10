from flask import request, jsonify, Blueprint
from api.models.users import Users
from api import bcrypt

api = Blueprint('login_api', __name__)


@api.route("/login", methods=["POST"])
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

        if user is None or not bcrypt.check_password_hash(user.password, password):
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


@api.route("/hash_password", methods=["POST"])
def hash_password():

    data = request.get_json()
    password = data.get("password")

    if not password:
        response = jsonify({
            "message": "Empty data received",
            "user_message": "Please fill all the info"
        }), 400
    else:
        pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")
        response = jsonify({
            "pw_hash": pw_hash,
            "message": "Password hashed successfully",
            "user_message": "Password hashed successfully"
        }), 200

    return response
