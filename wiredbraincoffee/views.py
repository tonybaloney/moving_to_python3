from flask import render_template, request

from wiredbraincoffee import app
from wiredbraincoffee.controllers.home import HomeController
from wiredbraincoffee.controllers.shop import ShopController
from wiredbraincoffee.controllers.stores import StoresController


@app.route('/')
def index():
    controller = HomeController()
    model = controller.view(request)
    return render_template('home.html', model=model)


@app.route('/shop/')
def shop():
    controller = ShopController()
    model = controller.view(request)
    return render_template('shop.html', model=model)


@app.route('/shop/<int:item_id>/')
def shop_for(item_id):
    controller = ShopController()
    model = controller.view_item(request, id=item_id)
    return render_template('shop_item.html', model=model)


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/stores/')
def stores():
    controller = StoresController()
    model = controller.view(request)
    return render_template('stores.html', model=model)
