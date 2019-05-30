from flask import Flask, request, json
app = Flask(__name__)


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
        response = app.response_class(
            response=json.dumps({
                "message": "Empty data received",
                "user_message": "Please fill all the info"
            }),
            status=400,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({
                "name": name,
                "email": email,
                "phone_number": phone_number
            }),
            status=200,
            mimetype='application/json'
        )
    return response
