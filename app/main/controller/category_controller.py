from flask import request
from flask_restplus import Resource

from ..util.decorators import admin_token_required
from ..util.category_dto import CategoryDto
from ..service.category_service import save_new_category, get_all_categories, get_a_category

api = CategoryDto.api
_category = CategoryDto.category

@api.route('/')
class CategoryList(Resource):
    @api.doc('list_of_all_categories')
    @api.marshal_list_with(_category, envelope='data')
    def get(self):
        """List all categories"""
        return get_all_categories()

    @api.response(201, 'Category successfully Created.')
    @api.doc('create a new category')
    @admin_token_required
    @api.expect(_category, validate=True)
    def post(self):
        """Creates a new category"""
        data = request.json
        return save_new_category(data=data)

@api.route('/<id>')
@api.param('id', 'The Category identifier')
@api.response(404, 'Category not found.')

class Category(Resource):
    @api.doc('get a category')
    @api.marshal_with(_category)
    def get(self, id):
        """get a category given its identifier"""
        category = get_a_category(id)
        if not category:
            api.abort(404)
        else:
            return category
