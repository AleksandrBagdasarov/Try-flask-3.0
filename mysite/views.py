from flask import redirect, render_template, url_for
from mysite.models import Product


def home():
    products = Product.query.all()
    return render_template('home.html', title='Home', products=products)


def product_details(slug):
    product = Product.query.filter(Product.slug==slug).first()
    return render_template('product_details.html', title='Details', product=product)
