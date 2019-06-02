from api import ma
from api.models.photographers import Photographers


class PhotographersSchema(ma.ModelSchema):
    class Meta:
        model = Photographers


photographers_schema = PhotographersSchema(strict=True, many=True)
