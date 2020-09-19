from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.v1.resources import users, expenses

APP = Flask(__name__)
api = Api(APP)

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(APP)

@APP.before_first_request
def create_tables():
    db.create_all()

api.add_resource(users.UserRegistration, '/registration')
api.add_resource(users.UserLogin, '/login')
api.add_resource(users.UserLogoutAccess, '/logout/access')
api.add_resource(users.UserLogoutRefresh, '/logout/refresh')
api.add_resource(users.TokenRefresh, '/token/refresh')
api.add_resource(users.AllUsers, '/users')
api.add_resource(expenses.Expenses, '/expenses')

if __name__ == "__main__":
    APP.run(debug=True, port=5000)