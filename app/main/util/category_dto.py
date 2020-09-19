from flask_restplus import Namespace, fields

class CategoryDto:
    api = Namespace('category', description='Category related operations')
    category = api.model('category', {
        'name': fields.String(required=True, description='Category Name'),
        'slug': fields.String(description='Category Slug'),
    })
