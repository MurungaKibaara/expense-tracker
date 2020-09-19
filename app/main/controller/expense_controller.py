from flask import request
from flask_restplus import Resource

from ..util.decorators import token_required
from ..util.expense_dto import ExpenseDto
from ..service.expense_service import save_new_expense, get_all_expenses, get_an_expense

api = ExpenseDto.api
_expense = ExpenseDto.expense


@api.route('/')
class ExpenseList(Resource):
    @api.doc('list_of_all_expenses')
    @token_required
    @api.marshal_list_with(_expense, envelope='data')
    def get(self, current_user):
        """List all added expenses"""
        return get_all_expenses(current_user)

    @api.response(201, 'Expense successfully Added.')
    @token_required
    @api.doc('create a new expense')
    @api.expect(_expense, validate=True)
    def post(self, current_user):
        """Creates a new expense """
        data = request.json
        return save_new_expense(current_user, data=data)

@api.route('/<id>')
@api.param('id', 'The Expense identifier')
@api.response(404, 'Expense not found.')
class Expense(Resource):
    @api.doc('Get an expense.')
    @token_required
    @api.marshal_with(_expense)
    def get(self, current_user, id):
        """get a expense given its identifier"""
        expense = get_an_expense(current_user, id)
        if not expense:
            api.abort(404)
        else:
            return expense
