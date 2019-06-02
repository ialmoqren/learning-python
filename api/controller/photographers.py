from flask import jsonify
from api.schemas.photographers_schema import photographers_schema
from api.models.photographers import Photographers
from api import app


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
