from flask_restplus import Namespace, fields

class ExpenseDto:
    api = Namespace('expense', description='expense related operations')
    expense = api.model('expense', {
        'name': fields.String(required=True, description='Expense Name'),
        'category_id': fields.Integer(required=True,description='Expense Category'),
        'user_id': fields.Integer(description='user/Author Identifier'),
        'date_posted': fields.String(description='Expense Post date'),
        'slug': fields.String(description='Expense Slug'),
        'amount': fields.Float(required=True, description='Expense Amount/Cost'),
    })
