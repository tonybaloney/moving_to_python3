from flask import render_template, request

from wiredbraincoffee import app
from wiredbraincoffee.controllers import home


@app.route('/')
def index():
    controller = home.HomeController()
    model = controller.view(request)
    return render_template('home.html', model=model)

@app.route('/shop/')
def shop():
    return render_template('shop.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')
