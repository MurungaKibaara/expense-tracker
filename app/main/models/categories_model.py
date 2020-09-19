from slugify import slugify
from .. import db

class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True)
    slug = db.Column(db.String(255))

    def __repr__(self):
        return f"{self.name}"
    
    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super().__init__(*args, **kwargs)
