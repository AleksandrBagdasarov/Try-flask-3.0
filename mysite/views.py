from flask import redirect, render_template, request, url_for
from mysite.models import Product, Tag


def home(previous_sort=None, sorted_by=None):
    tags = Tag.query.all()
    q = request.args.get('q')
    if q or sorted_by:
        if q:
            products = Product.query.filter(Product.title.contains(q))
            previous_sort = products
        if sorted_by and previous_sort:
            if sorted_by == 'top':
                pass
            elif sorted_by == 'featured':
                products = previous_sort.order_by(Product.id)

            elif sorted_by == 'low':
                pass
            elif sorted_by == 'high':
                pass
        elif sorted_by:
            if sorted_by == 'top':
                pass
            elif sorted_by == 'featured':
                products = Product.query.order_by(Product.id)

            elif sorted_by == 'low':
                pass
            elif sorted_by == 'high':
                pass      
    else:
        products = Product.query

    products = products.all()    
    return render_template('home.html', title='Home', products=products, tags=tags, previous_sort=previous_sort)


def product_details(slug):
    product = Product.query.filter(Product.slug==slug).first()
    return render_template('product_details.html', title='Product Details', product=product)


def tag_details(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    products = tag.products.all()
    return render_template('tag_details.html', title='Tag Details', products=products, tag=tag)