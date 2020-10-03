from slugify import slugify
import uuid
from .. import db

class ExpenseModel(db.Model):
    """ Expenses Model for storing expense related details """
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_expense = db.Column(db.Date, nullable=False)
    create_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('CategoryModel', backref='category')

    def __repr__(self):
        return f"{self.name}"

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(str(uuid.uuid4()) + kwargs.get('name', ''))
        super().__init__(*args, **kwargs)
