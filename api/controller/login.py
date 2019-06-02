from flask import request, jsonify
from api import app
from api.models.users import Users


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
