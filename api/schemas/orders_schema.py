from api import ma
from api.models.orders import Orders


class OrdersSchema(ma.ModelSchema):
    class Meta:
        model = Orders


orders_schema = OrdersSchema(strict=True, many=True)
