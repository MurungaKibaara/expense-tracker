from datetime import datetime

from app.main import db
from app.main.models.categories_model import CategoryModel as Category


def save_new_category(data):

    new_category = Category(
        name=data['name'],
    )
    try:
        save_changes(new_category)
        response_object = {
            'status': 'success',
            'message': 'Category Added!'
        }  
        return response_object, 201
    except:
        response_object = {
            'status': 'fail',
            'message': 'Something happended. Please try again.',
        }
        return  response_object, 400
  
def get_all_categories():
    return Category.query.all()

def get_a_category(id):
    return Category.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
