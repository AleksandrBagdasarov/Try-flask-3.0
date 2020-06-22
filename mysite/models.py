from datetime import datetime
from mysite import db
import re


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


product_tags = db.Table('product_tags',
                            db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
                            db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                            )


class Product(db.Model):
    id =            db.Column(db.Integer, primary_key=True)
    title =         db.Column(db.String(32, collation='NOCASE'))
    slug =          db.Column(db.String(140, collation='NOCASE'), unique=True)
    discription =   db.Column(db.Text)
    created =       db.Column(db.DateTime, default=datetime.utcnow())
    img =           db.Column(db.String(20), nullable=False, default='default_product.jpg')
    tags =          db.relationship('Tag', secondary='product_tags', backref=db.backref('products', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
    
    def __repr__(self):
        return f"Product('{self.title}','{self.created}','{self.discription}')"


class Tag(db.Model):
    id =            db.Column(db.Integer, primary_key=True)
    name =          db.Column(db.String(32, collation='NOCASE'))
    slug =          db.Column(db.String(140, collation='NOCASE'), unique=True)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)

    def __repr__(self):
        return f"Tag('{self.id}','{self.name}')"


class User(db.Model):
    id =            db.Column(db.Integer, primary_key=True)
    mail =          db.Column(db.String(128), unique=True, nullable=False)
    passwrod =      db.Column(db.String(128), nullable=False)
    created =       db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    img =           db.Column(db.String(20), nullable=False, default='default_user.jpg')

    def __repr__(self):
        return f"User('{self.mail}','{self.created}')"