from flask import Flask, request, json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/register", methods=["POST"])
def register():
    name = request.args.get("name")
    email = request.args.get("email")
    phone_number = request.args.get("phone_number")

    print(name, email, phone_number)

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
