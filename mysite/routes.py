from mysite import app
from mysite.views import home, product_details, tag_details



app.add_url_rule('/',                   view_func=home,                    methods=['GET',])
app.add_url_rule('/product/<slug>',     view_func=product_details,         methods=['GET',])
app.add_url_rule('/tag/<slug>',         view_func=tag_details,             methods=['GET',])