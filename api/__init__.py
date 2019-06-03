from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import config

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)

    from api.controller.login import api as login_api_blueprint
    from api.controller.order import api as order_api_blueprint
    from api.controller.orders import api as orders_api_blueprint
    from api.controller.photographers import api as photographers_api_blueprint
    from api.controller.register import api as register_api_blueprint

    app.register_blueprint(login_api_blueprint)
    app.register_blueprint(order_api_blueprint)
    app.register_blueprint(orders_api_blueprint)
    app.register_blueprint(orders_api_blueprint)
    app.register_blueprint(photographers_api_blueprint)
    app.register_blueprint(register_api_blueprint)

    app.run(host='0.0.0.0', port=5000, debug=True)
    return app

from api.controller.login import login
from api.controller.order import order
from api.controller.orders import orders
from api.controller.photographers import photographers
from api.controller.register import register
