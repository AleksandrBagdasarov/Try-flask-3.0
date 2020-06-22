from flask import redirect, render_template, request, url_for
from mysite.models import Product, Tag


def home():
    q = request.args.get('q')
    if q:
        products = Product.query.filter(Product.title.contains(q)).all()
    else:
        products = Product.query.all()
    tags = Tag.query.all()
    return render_template('home.html', title='Home', products=products, tags=tags)


def product_details(slug):
    product = Product.query.filter(Product.slug==slug).first()
    return render_template('product_details.html', title='Product Details', product=product)


def tag_details(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    products = tag.products.all()
    return render_template('tag_details.html', title='Tag Details', products=products, tag=tag)