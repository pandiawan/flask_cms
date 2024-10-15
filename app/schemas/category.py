from marshmallow import Schema, fields, validate


class CategorySchema(Schema):
    _id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
