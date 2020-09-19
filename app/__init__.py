from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.expense_controller import api as expense_ns
from .main.controller.category_controller import api as category_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='EXPENSE TRACKER API',
          version='1.0',
          description='expense tracker web service'
          )

api.add_namespace(user_ns, path='/users')
api.add_namespace(auth_ns)
api.add_namespace(expense_ns, path='/expenses')
api.add_namespace(category_ns, path='/category')
