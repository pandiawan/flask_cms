from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    _id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(max=100))
    email = fields.Email(required=True, validate=validate.Email())
    username = fields.Str(required=True, validate=validate.Length(max=100))
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
