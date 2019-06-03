from flask import request, jsonify, Blueprint
from api.schemas.orders_schema import orders_schema
from api.models.orders import Orders

api = Blueprint('orders_api', __name__)


@api.route("/orders")
def orders():

    all_orders = Orders.query.all()

    if not all_orders:
        return jsonify({
            "message": "No data",
            "user_message": "There are no orders"
        }), 200
    else:
        return orders_schema.jsonify(all_orders), 200
