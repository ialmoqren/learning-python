from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

from api.controller.login import *
from api.controller.order import *
from api.controller.orders import *
from api.controller.photographers import *
from api.controller.register import *
