from datetime import datetime
from mysite import db
import re


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Product(db.Model):
    id =            db.Column(db.Integer, primary_key=True)
    title =         db.Column(db.String(32, collation='NOCASE'))
    slug =          db.Column(db.String(140, collation='NOCASE'), unique=True)
    discription =   db.Column(db.Text)
    created =       db.Column(db.DateTime, default=datetime.utcnow())
    img =           db.Column(db.String(20), nullable=False, default='default_product.jpg')

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
    
    def __repr__(self):
        return f"User('{self.title}','{self.created}','{self.discription}')"


class User(db.Model):
    id =            db.Column(db.Integer, primary_key=True)
    mail =          db.Column(db.String(128), unique=True, nullable=False)
    passwrod =      db.Column(db.String(128), nullable=False)
    created =       db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    img =           db.Column(db.String(20), nullable=False, default='default_user.jpg')

    def __repr__(self):
        return f"User('{self.mail}','{self.created}')"