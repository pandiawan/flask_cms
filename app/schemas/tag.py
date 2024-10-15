from marshmallow import Schema, fields, validate


class TagSchema(Schema):
    _id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
