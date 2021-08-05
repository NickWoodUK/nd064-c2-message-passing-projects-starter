from marshmallow import Schema, fields

from modules.api.app.udaconnect.models import Person
from modules.locationApi.app.udaconnect.schemas import LocationSchema


class PersonSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    company_name = fields.String()

    class Meta:
        model = Person


class ConnectionSchema(Schema):
    location = fields.Nested(LocationSchema)
    person = fields.Nested(PersonSchema)
