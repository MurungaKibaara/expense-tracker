from datetime import datetime

from app.main import db
from app.main.models.expenses_model import ExpenseModel as Expense

def save_new_expense(current_user, data):
    current_user_id = current_user['user_id']
    new_expense = Expense(
        user_id=current_user_id,
        name=data['name'],
        amount=data['amount'],
        category_id=data['category_id'],
        date_posted=str(datetime.now()),
    )
    try:
        save_changes(new_expense)
        response_object = {
            'status': 'success',
            'message': 'Expense Added!'
        }  
        return response_object, 201
    except:
        response_object = {
            'status': 'fail',
            'message': 'Something happended. Please try again.',
        }
        return  response_object, 400
  
def get_all_expenses(current_user):
    current_user_id = int(current_user['user_id'])
    return Expense.query.filter_by(user_id=current_user_id).all()

def get_an_expense(current_user, id):
    current_user_id = current_user['user_id']
    print(int(current_user_id))
    return Expense.query.filter_by(id=id, user_id=current_user_id).all()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
