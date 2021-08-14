from marshmallow import Schema, fields

class ConnectionSchema(Schema):
    location = fields.Nested(LocationSchema)
    person = fields.Nested(PersonSchema)
