from marshmallow import Schema, fields, validates, ValidationError
from bson import ObjectId
from app.services.category import CategoryService


class PostSchema(Schema):
    _id = fields.Str(dump_only=True)
    title = fields.Str(required=True, validate=lambda t: 0 < len(t) <= 200)
    content = fields.Str(required=True)
    image = fields.Str(required=True)  # File path as string
    author = fields.Str(required=True)  # Reference to User
    category_id = fields.Str(required=True)  # Reference to Category
    tags = fields.List(fields.Str(), required=True)
    published = fields.DateTime(dump_only=True)  # Automatically set during creation

    @validates('category_id')
    def validate_category(self, value):
        # Check if the category exists in the database
        if not ObjectId.is_valid(value):
            raise ValidationError('Invalid category ID.')

        category = CategoryService().get_by_id(value)
        if not category:
            raise ValidationError('Category does not exist.')
